from qa_engine import generate_answer

if __name__ == "__main__":
    pdf_file = "C:\\Users\\sudar\\OneDrive\\Desktop\\UNIT-4 SP.pdf"  # Replace with your PDF path
    question = input("Enter your question: ")
    answer = generate_answer(pdf_file, question)
    print("\nAnswer:", answer)
