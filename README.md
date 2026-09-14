# Trinary Opinion Generator

An educational experiment that prompts a local language model for positive, neutral, and negative perspectives, then combines simple word-count sentiment scores.

**Status:** Historical prototype. This is a demonstration of prompt orchestration and heuristic aggregation, not a validated decision or forecasting system.

## Actual workflow

1. Read a topic from the command line.
2. Generate three responses sequentially using role-specific prompts.
3. Count exact whitespace-separated matches against small positive and negative word lists.
4. Average the three scores with equal weights.
5. Print an optimistic, pessimistic, or neutral label based on the score's sign.

All three instances use the same Ollama model, `llama3`. The code does not configure different models or role-specific temperatures. Diversity comes from the prompts and any model sampling variation.

## Source

[multi_llm_ensemble.py](multi_llm_ensemble.py) separates response generation, sentiment scoring, aggregation, and CLI handling. It includes logging and error handling.

## Local setup reference

```bash
git clone https://github.com/Dolvido/TrinaryOpinionGenerator.git
cd TrinaryOpinionGenerator
```

Run an Ollama service with `llama3` available, or update the model names in `MODELS`. Restore an environment compatible with the source's `langchain_community.llms.Ollama`, `PromptTemplate`, and `LLMChain` imports before running:

```bash
python multi_llm_ensemble.py
```

The repository has no `requirements.txt` or lockfile. Dependency versions and current runtime compatibility have not been verified.

## Limitations and useful follow-up work

- The word-count scorer does not handle negation, context, or punctuation robustly.
- The final label measures the wording of generated responses rather than whether their reasoning or evidence is sound.
- Equal weights and role prompts do not establish reduced bias, factual consensus, or improved decision quality.
- Generation errors are returned as strings and currently enter the same aggregation path as successful responses.
- No automated tests, evaluation dataset, or comparison against a single-response baseline are included.

A useful next step would be tests for the deterministic scorer and explicit handling of failed generation, followed by a documented evaluation of any aggregation changes.

No model calls or runtime tests were performed for this documentation refresh.
