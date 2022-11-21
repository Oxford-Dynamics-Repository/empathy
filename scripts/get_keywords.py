# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script sets up the TAPAS model.

from transformers import TapasTokenizer, TapasForQuestionAnswering
from return_database import return_database


def get_keywords(query, model, tokenizer):
    table = return_database()
    queries = [query]

    inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="pt")
    outputs = model(**inputs)

    predicted_answer_coordinates, predicted_aggregation_indices = tokenizer.convert_logits_to_predictions(
        inputs, outputs.logits.detach(), outputs.logits_aggregation.detach())

    id2aggregation = {0: "NONE", 1: "SUM", 2: "AVERAGE", 3: "COUNT"}
    aggregation_predictions_string = [id2aggregation[x] for x in predicted_aggregation_indices]

    answers = []
    for coordinates in predicted_answer_coordinates:
        if len(coordinates) == 1:
            # Selecting only a single cell.
            answers.append(table.iat[coordinates[0]])
        else:
            # Selecting multiple cells.
            cell_values = []
            for coordinate in coordinates:
                cell_values.append(table.iat[coordinate])
            answers.append(", ".join(cell_values))

    for query, answer, predicted_agg in zip(queries, answers, aggregation_predictions_string):
        if predicted_agg == "NONE":
            return(answer)
        else:
            return(predicted_agg + " > " + answer)

def main():
    keyword = get_keywords(query)


if __name__ == '__main__':
    main()