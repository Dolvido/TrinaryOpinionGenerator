import sys
import logging

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# -----------------------------------------------------------------------------
# Logging configuration for debugging and error tracking.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------------------------------------------
# Prompt templates for each role
PROMPT_TEMPLATES = {
    "positive": "In the context of '{topic}', provide an optimistic and supportive analysis that emphasizes positive aspects.",
    "neutral": "In the context of '{topic}', provide a balanced, factual, and objective analysis.",
    "negative": "In the context of '{topic}', provide a critical and cautious analysis focusing on potential drawbacks and negative aspects."
}

# -----------------------------------------------------------------------------
# Initialize separate LLM instances for each role with role-specific parameters.
try:
    MODELS = {
        "positive": Ollama(model="llama3"),
        "neutral": Ollama(model="llama3"),
        "negative": Ollama(model="llama3")
    }
except Exception as e:
    logging.error("Failed to initialize LLM models: %s", e)
    sys.exit(1)

# -----------------------------------------------------------------------------
def generate_response(role: str, topic: str) -> str:
    """
    Generate a response for a given role and topic using the appropriate LLM.

    Args:
        role (str): Role of the response ('positive', 'neutral', or 'negative').
        topic (str): The topic to analyze.

    Returns:
        str: The generated response from the LLM.
    """
    logging.info("Generating response for role: %s, topic: %s", role, topic)
    try:
        # Select appropriate prompt template based on role.
        if role not in PROMPT_TEMPLATES:
            raise ValueError(f"Invalid role provided: {role}")

        prompt_str = PROMPT_TEMPLATES[role]
        prompt = PromptTemplate(template=prompt_str, input_variables=["topic"])

        # Select the corresponding LLM instance.
        llm = MODELS.get(role)
        if not llm:
            raise ValueError(f"No LLM configured for role: {role}")

        # Create and run the LLM chain.
        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.invoke({"topic": topic})
        # If the new API returns a dict, extract the text using the key "text".
        if isinstance(result, dict) and "text" in result:
            response_text = result["text"]
        else:
            response_text = result
        logging.info("Successfully generated response for role '%s'.", role)
        return response_text.strip()
    except Exception as e:
        logging.error("Error generating response for role '%s': %s", role, e)
        return f"Error generating response for {role}: {e}"

# -----------------------------------------------------------------------------
def analyze_sentiment(text: str) -> float:
    """
    Performs basic sentiment analysis based on a word count approach.

    Args:
        text (str): The text to be analyzed.

    Returns:
        float: A sentiment score (positive count minus negative count).
    """
    positive_words = {
        "good", "great", "excellent", "optimistic", "supportive",
        "beneficial", "amazing", "positive", "impressive", "favorable"
    }
    negative_words = {
        "bad", "poor", "terrible", "caution", "negative",
        "critical", "doubtful", "unfavorable", "disappointing"
    }

    words = text.lower().split()
    pos_count = sum(word in positive_words for word in words)
    neg_count = sum(word in negative_words for word in words)
    score = pos_count - neg_count
    logging.debug("Text analyzed for sentiment. Score: %s", score)
    return score

# -----------------------------------------------------------------------------
def aggregate_responses(responses: dict) -> str:
    """
    Aggregates responses mathematically based on sentiment scores.

    Each role's response is analyzed to get a sentiment score, and a weighted
    average is computed. The final opinion is mapped back from the average score.

    Args:
        responses (dict): Dictionary with keys 'positive', 'neutral', and 'negative'.

    Returns:
        str: A final aggregated opinion.
    """
    try:
        logging.info("Starting aggregation of responses.")
        scores = {}
        weights = {"positive": 1.0, "neutral": 1.0, "negative": 1.0}
        
        for role, response in responses.items():
            score = analyze_sentiment(response)
            scores[role] = score
            logging.info("Sentiment score for '%s': %s", role, score)

        # Compute weighted average of sentiment scores.
        weighted_sum = sum(weights[role] * scores.get(role, 0) for role in weights)
        total_weight = sum(weights.values())
        avg_score = weighted_sum / total_weight
        logging.info("Computed weighted average sentiment score: %s", avg_score)

        # Map average score to final opinion.
        if avg_score > 0:
            final_opinion = "The ensemble analysis suggests an optimistic perspective."
        elif avg_score < 0:
            final_opinion = "The ensemble analysis suggests a pessimistic perspective."
        else:
            final_opinion = "The ensemble analysis suggests a balanced, neutral perspective."

        return final_opinion
    except Exception as e:
        logging.error("Error during aggregation: %s", e)
        return f"Error aggregating responses: {e}"

# -----------------------------------------------------------------------------
def main():
    """
    Main function to run the multi-LLM ensemble pipeline.

    - Accepts a topic from the user.
    - Generates role-specific responses.
    - Aggregates responses to form a final synthesized opinion.
    """
    try:
        topic = input("Enter a topic for analysis: ").strip()
        if not topic:
            print("Topic cannot be empty.")
            return

        responses = {}
        # Generate responses for each role.
        for role in ["positive", "neutral", "negative"]:
            responses[role] = generate_response(role, topic)

        # Print each individual role response.
        print("\nIndividual Role Responses:")
        for role, text in responses.items():
            print(f"\n[{role.capitalize()} View]:\n{text}")

        # Compute and print the final aggregated opinion.
        final_opinion = aggregate_responses(responses)
        print("\nFinal Aggregated Opinion:")
        print(final_opinion)
    except Exception as e:
        logging.error("An error occurred in main execution: %s", e)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 
