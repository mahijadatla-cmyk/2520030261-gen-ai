import torch
import csv
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM

# ------------------------------------------------
# 1. Load GPT-2 Language Model
# ------------------------------------------------

MODEL_NAME = "openai-community/gpt2"

def main():

    print("==============================================")
    print(" WEEK 7 - NEXT TOKEN PROBABILITY ANALYSIS")
    print("==============================================")

    print("\nLoading GPT-2 model...", flush=True)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    model.eval()

    print("GPT-2 model loaded successfully!", flush=True)

    # ------------------------------------------------
    # 2. Define Input Prompts
    # ------------------------------------------------

    prompts = [
        "The cat is",
        "Artificial intelligence is",
        "India is a",
        "Machine learning helps"
    ]

    TOP_K = 5
    results = []

    # ------------------------------------------------
    # 3. Calculate Next Token Probabilities
    # ------------------------------------------------

    for prompt in prompts:

        print("\n" + "=" * 60)
        print("PROMPT:", prompt)
        print("=" * 60)

        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt")

        print("Input Token IDs:", inputs["input_ids"][0].tolist())

        # Get model predictions
        with torch.no_grad():
            outputs = model(**inputs)

        # Get logits for next token
        logits = outputs.logits[0, -1, :]

        # Convert logits to probabilities
        probabilities = torch.softmax(logits, dim=-1)

        # Get top 5 predictions
        top_probs, top_ids = torch.topk(probabilities, TOP_K)

        print("\nTop", TOP_K, "Next Token Candidates:")
        print("-" * 60)

        for rank, (token_id, probability) in enumerate(
            zip(top_ids, top_probs), start=1
        ):

            token = tokenizer.decode([token_id.item()])
            prob = probability.item()

            print(
                f"Rank: {rank} | "
                f"Token: {repr(token)} | "
                f"Probability: {prob:.6f}"
            )

            results.append([
                prompt,
                rank,
                token,
                token_id.item(),
                round(prob, 6)
            ])

    # ------------------------------------------------
    # 4. Save Results to CSV
    # ------------------------------------------------

    filename = "week7_probability_results.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Prompt",
            "Rank",
            "Candidate Token",
            "Token ID",
            "Probability"
        ])

        writer.writerows(results)

    print("\n" + "=" * 60)
    print("EXPERIMENT COMPLETED SUCCESSFULLY!")
    print("Total predictions:", len(results))
    print("Results saved to:", filename)
    print("=" * 60)


if __name__ == "__main__":
    main()
