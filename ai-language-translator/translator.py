
from transformers import MarianMTModel, MarianTokenizer

MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

print("Loading AI Translation Model...")

tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

print("Model loaded successfully!")


def translate_text(text):
    if not text.strip():
        return "Please enter some text."

    # Convert input text into tokens
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    # Generate translated tokens
    translated = model.generate(**inputs)

    # Convert tokens into readable text
    result = tokenizer.decode(
        translated[0],
        skip_special_tokens=True
    )

    return result


# Test our AI model
if __name__ == "__main__":
    sentence = "Hello, how are you?"

    print("\nEnglish:", sentence)

    translation = translate_text(sentence)

    print("French:", translation)
