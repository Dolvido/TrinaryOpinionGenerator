# Multi-LLM Ensemble Analysis for Topic Sentiment Aggregation

This project demonstrates a multi-LLM ensemble approach using LangChain to generate diverse perspectives on a given topic. It leverages three separate LLM instances—each with a distinct role (positive, neutral, negative)—to produce role-specific analyses. A simple sentiment analysis then aggregates these responses into a final synthesized opinion.

## Overview

The project is designed to:
- **Generate Role-Specific Responses:** For a given topic, three different LLM configurations produce analyses from positive, neutral, and negative perspectives.
- **Perform Sentiment Analysis:** A basic word count-based sentiment analysis function scores each response.
- **Aggregate Perspectives:** The individual sentiment scores are combined using a weighted average to produce a final opinion (optimistic, pessimistic, or neutral).

When you run the script and input a topic such as `"web3"`, the tool outputs individual role responses along with an aggregated sentiment—demonstrated below in the sample output.

## Key Features

- **Diverse Perspectives:** Leverages three separate language models with role-specific parameters (temperature settings) to ensure diversity in responses.
- **Customizable Prompt Templates:** Uses distinct prompt templates for each role (positive, neutral, negative) to steer the model’s analysis.
- **Simple Sentiment Aggregation:** Implements a basic sentiment analysis function based on positive and negative word counts.
- **Logging & Error Handling:** Provides detailed logging for easier debugging and error tracking.
- **Modular Design:** Functions are separated by responsibility (e.g., generating responses, analyzing sentiment, aggregating results), making it easy to modify or extend.

## Critical Functioning

### 1. **Response Generation (`generate_response`)**
   - **Purpose:** For each role, this function:
     - Selects the appropriate prompt template.
     - Invokes an LLM chain with a role-specific configuration.
     - Returns the generated text.
   - **Key Details:**  
     - Uses role-specific temperature settings to control creativity.
     - Handles exceptions and logs errors if an invalid role is passed or if LLM generation fails.

### 2. **Sentiment Analysis (`analyze_sentiment`)**
   - **Purpose:** Analyzes each response using a simple word count method.
   - **How It Works:**  
     - Counts occurrences of words from predefined positive and negative sets.
     - Calculates a sentiment score as the difference between positive and negative counts.
   - **Rationale:** Provides a straightforward way to numerically compare the tone of each LLM’s response.

### 3. **Response Aggregation (`aggregate_responses`)**
   - **Purpose:** Aggregates the individual sentiment scores from the role responses.
   - **How It Works:**  
     - Computes a weighted average of the scores (equal weights are used in this example).
     - Maps the average score to a final opinion (optimistic if positive, pessimistic if negative, or neutral if zero).
   - **Benefits:**  
     - Combines multiple perspectives into a single, synthesized opinion.
     - Helps in identifying the overall sentiment by mathematically balancing the distinct views.

### 4. **Main Execution (`main`)**
   - **Purpose:** Orchestrates the entire workflow:
     - Prompts the user for a topic.
     - Generates role-specific responses.
     - Displays individual responses.
     - Aggregates the responses and prints the final opinion.
   - **User Interaction:**  
     - The user inputs a topic (e.g., `"web3"`), and the script outputs detailed analyses and an aggregated sentiment summary.

## Sample Output

When the input topic is `"web3"`, the output might look similar to the following:

```
Enter a topic for analysis: web3

Individual Role Responses:

[Positive View]: The thrilling world of web3! As we embark on this exciting journey, let's focus on the bright side of this innovative space. ...

[Neutral View]: Web3: A Balanced Analysis of the Emerging Landscape Introduction: Web3 is an umbrella term for the next generation of the internet, focusing on decentralization, blockchain technology, and cryptocurrencies. ...

[Negative View]: The tantalizing promise of "web3" - a decentralized, blockchain-based internet that could revolutionize online interactions...

Final Aggregated Opinion: The ensemble analysis suggests an optimistic perspective.
```


## Why Use This Project?

- **Educational Value:**  
  - Learn how to orchestrate multiple LLMs using role-specific prompt engineering.
  - Understand a basic approach to sentiment analysis and how it can inform aggregated decisions.
  
- **Diverse Insights:**  
  - Combining different viewpoints (positive, neutral, negative) can lead to more balanced and nuanced analyses.
  - Useful for scenarios where a single-perspective response might be biased or incomplete.
  
- **Extensibility:**  
  - The modular design makes it easy to extend the project—for instance, adding more roles, integrating advanced sentiment analysis, or using different LLMs.
  
- **Practical Applications:**  
  - Can be adapted for use cases such as market analysis, risk assessment, or any scenario where multi-faceted opinions are beneficial.

## Installation

1. **Clone the Repository:**

   ```
   git clone https://github.com/yourusername/multi-llm-ensemble.git
   cd multi-llm-ensemble
   ```
2. **Set Up a Virtual Environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```
  #Note: Ensure that you have installed the required versions of LangChain and any other dependencies. The code uses deprecated classes (e.g., Ollama and LLMChain), so check the latest documentation or consider updating as suggested by the deprecation warnings.


## Usage
Run the script from the command line:
```
python multi_llm_ensemble.py
```
Then, follow the prompt to enter a topic for analysis.

