#  LLM Evaluation Using Structured Cricket Dataset

This task evaluates the ability of a Large Language Model (LLM) to answer progressively complex analytical questions when provided with a compact, real-world dataset. The dataset used is based on bowling statistics from ICC World Cup 2023, filtered to only include bowlers from the winning team in each match.

---

##  Objective

To assess the reasoning, aggregation, filtering, and interpretive capabilities of an LLM when given a clean, tabular dataset.

The goal is **not cricket analysis**, but rather to explore **how effectively an LLM can extract insights** from structured data using natural language prompts.

---

##  Dataset Details

- Dataset is merged from match winnning details and bowling stats from ICC World Cup 23 to keep dataset simple and intact
- **File**: `llm_ready_bowling_with_match_context.csv`
- **Structure**: Each row represents a bowler’s performance in a match. Includes:
  - Match context: teams, winner, date, venue
  - Bowler stats: overs, maidens, runs, wickets, economy
- **Filtered**: Includes only bowling performances from the **winning team** to simplify reasoning scope.

---

##  Prompted Questions and LLM Responses

### Basic Aggregation
> Who took the most wickets in the tournament?

-  Correctly identified **Adam Zampa** (22 wickets), verified manually.

> Which bowler bowled the most overs across all winning matches?

-  Correctly identified **Kuldeep Yadav** (83.1 overs), verified in Pandas.

> How many bowlers bowled more than 7 overs?

-  Answered **73 bowlers**, verified in Pandas.

---

### Intermediate Reasoning
> Which team had the most economical bowling performance on average?

-  Identified **Netherlands** as the most economical (avg economy: 4.28), verified in Pandas

> List all bowlers who took 3 or more wickets in a match.

-  Returned an accurate list with match-wise breakdown., verified manually.

---

### Advanced Analytical Prompts
> Who was the most improved bowler over the tournament? (based on economy trend)

-  Correctly calculated linear trend and identified **Logan van Beek** as the most improved.

> If India could improve one bowler to win 2 extra matches, who should it be?

-  Identified **Mohammed Shami** (18 wickets, 5.13 econ) as the best strategic candidate.

> Was economy rate or wickets a stronger factor in match wins?

-  Correlation analysis was attempted, but due to limited data rows and some inconsistencies, results were inconclusive (`NaN` correlation).  
-  Qualitative insight suggests **wickets** have stronger influence on match outcome.

---

##  Comparison: ChatGPT vs Claude (Anthropic)

To evaluate LLM reasoning quality, the same analytical questions were asked to both **ChatGPT** and **Claude**. Here's how their answers compared:

### 1. Most Improved Bowler
- **ChatGPT** identified **Logan van Beek** as the most improved, using a linear regression on match-wise economy rate.
- **Claude** selected **Mehidy Hasan Miraz**, stating his economy dropped from 5.35 to 2.78, but did not show underlying data or regression logic.

### 2. Indian Player to Improve for 2 Extra Wins
- Both models selected **Mohammed Shami**.
- **Claude** emphasized his strike rate, economy potential, and match impact.
- **ChatGPT** provided statistical support: 18 wickets, 5.13 economy, and overs bowled — highlighting him as India’s most impactful bowler.

### 3. Economy Rate vs Wickets for Wins
- **ChatGPT** attempted correlation analysis but found inconclusive statistical values (`NaN`) — pointing to data limitations.
- **Claude** claimed that **economy rate was the stronger factor**, but without statistical proof.

---

 **Conclusion**:
- **ChatGPT-4** showed the strongest analytical capability and transparency.
- **ChatGPT-3** provided reasonable outputs but lacked deep statistical logic.
- **Claude** excelled in intuitive and readable storytelling but skipped detailed computation.

---

##  Summary

This project demonstrates that modern LLMs, when provided with structured CSV data and clear prompts, can perform reliable **descriptive**, **comparative**, and even **strategic** analysis — showcasing their potential for lightweight data exploration without explicit coding.
