import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

class Agent:
    """
    Agent for summarizing study notes and generating quizzes from PDF documents.
    """
    def __init__(self, model: str = "gpt-4o-mini"):
        """
        Initializes the Agent with a specified OpenAI model.

        Args:
            model (str): The OpenAI model to use for generation tasks.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment or .env file.")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def extract_text_from_pdf(self, pdf_file_path: str) -> str:
        """
        Extracts text content from a given PDF file.

        Args:
            pdf_file_path (str): The path to the PDF file.

        Returns:
            str: The extracted text from the PDF. Returns an empty string if extraction fails.
        """
        try:
            with open(pdf_file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""

    def _chunk_text(self, text: str, max_tokens: int = 15000) -> list[str]:
        """
        Splits a long text into chunks that are unlikely to exceed the model's token limit.
        This is a simple implementation based on character count.

        Args:
            text (str): The input text.
            max_tokens (int): The approximate maximum tokens per chunk.

        Returns:
            list[str]: A list of text chunks.
        """
        # A rough approximation: 1 token ~ 4 characters
        max_chars = max_tokens * 3 
        
        if len(text) <= max_chars:
            return [text]

        chunks = []
        current_pos = 0
        while current_pos < len(text):
            end_pos = min(current_pos + max_chars, len(text))
            chunk = text[current_pos:end_pos]
            chunks.append(chunk)
            current_pos = end_pos
            
        return chunks

    def generate_summary(self, full_text: str) -> str:
        """
        Generates a bullet-point summary of the provided text.
        Handles long texts by summarizing chunks first.

        Args:
            full_text (str): The text to summarize.

        Returns:
            str: A formatted, bullet-point summary between 250-400 words.
        """
        if not full_text:
            return "The document is empty or text could not be extracted."

        chunks = self._chunk_text(full_text)
        
        summaries = []
        if len(chunks) > 1:
            for i, chunk in enumerate(chunks):
                print(f"Summarizing chunk {i+1}/{len(chunks)}...")
                system_prompt = "You are an expert academic summarizer."
                user_prompt = f"Provide a concise summary of the following text segment:\n\n---\n{chunk}\n---"
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.5,
                )
                summaries.append(response.choices[0].message.content)
            
            combined_summary_text = "\n\n".join(summaries)
        else:
            combined_summary_text = chunks[0]

        print("Generating final summary...")
        final_system_prompt = (
            "You are a skilled editor. Your task is to synthesize the provided text "
            "into a single, coherent, beautiful bullet-point summary."
        )
        final_user_prompt = (
            f"Based on the following text, generate a comprehensive bullet-point summary. "
            f"The summary should be well-structured, easy to read, and between 250 and 400 words. "
            f"Do not include any introductory or concluding phrases, just the bullet points.\n\n"
            f"---\n{combined_summary_text}\n---"
        )

        final_response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": final_system_prompt},
                {"role": "user", "content": final_user_prompt},
            ],
            temperature=0.7,
            max_tokens=1000,
        )
        return final_response.choices[0].message.content

    def generate_quiz(self, full_text: str) -> dict:
        """
        Generates a quiz from the full text, consisting of multiple-choice and short-answer questions.

        Args:
            full_text (str): The original text to base the quiz on.

        Returns:
            dict: A dictionary containing the quiz data, parsed from JSON.
        """
        if not full_text:
            return {}

        # Use a single, large chunk for quiz generation to ensure context.
        # This might fail for extremely large documents, but is better for question quality.
        chunk = self._chunk_text(full_text, max_tokens=16000)[0] 

        system_prompt = (
            "You are an expert quiz creator for students. Create a MCQs Or mixed-style quizzes based on the provided text. "
            "You must follow the specified JSON format exactly."
        )
        
        user_prompt = f"""
        From the original text below, generate a quiz with exactly 5 high-quality multiple-choice questions (MCQs) 3 and 3 short-answer questions.

        The output MUST be a single valid JSON object. Do not include any text or markdown before or after the JSON.

        JSON structure:
        {{
          "multiple_choice": [
            {{
              "question": "The question text.",
              "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
              }},
              "correct_answer": "A",
              "explanation": "A brief explanation of why this is the correct answer."
            }}
          ],
          "short_answer": [
            {{
              "question": "The short-answer question text.",
              "ideal_answer": "A concise, ideal answer to the question."
            }}
          ]
        }}

        Here is the text to use for quiz generation:
        ---
        {chunk}
        ---
        """

        print("Generating quiz...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.6,
        )

        try:
            quiz_content = response.choices[0].message.content
            quiz_data = json.loads(quiz_content)
            return quiz_data
        except (json.JSONDecodeError, IndexError) as e:
            print(f"Error parsing quiz JSON: {e}")
            print(f"Raw content received from API:\n{quiz_content}")
            return {}

if __name__ == '__main__':
    # Example usage for testing the agent directly
    # Make sure you have a .env file with your OPENAI_API_KEY
    # and a sample PDF file named 'sample.pdf' in the same directory.
    
    if not os.path.exists("sample.pdf"):
        print("Please create a 'sample.pdf' file to run this test.")
    else:
        print("Initializing agent...")
        agent = Agent()

        print("\nExtracting text from PDF...")
        pdf_text = agent.extract_text_from_pdf("sample.pdf")
        
        if pdf_text:
            print(f"Extracted {len(pdf_text)} characters.")

            print("\n--- Generating Summary ---")
            summary = agent.generate_summary(pdf_text)
            print("Summary:\n", summary)

            print("\n--- Generating Quiz ---")
            quiz = agent.generate_quiz(pdf_text)
            if quiz:
                print("Quiz Data (JSON):\n", json.dumps(quiz, indent=2))
            else:
                print("Failed to generate quiz.")
        else:
            print("Could not extract text from the PDF.")
