# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script sets up the TAPAS model.

from transformers import TapasTokenizer, TapasForQuestionAnswering
import pandas as pd

model_name = "google/tapas-base-finetuned-wtq"
model = TapasForQuestionAnswering.from_pretrained(model_name)
tokenizer = TapasTokenizer.from_pretrained(model_name)

data = {"Threats": ["Enemies", "Terrorists", "Men", "Women"], 
        "Number of people": ["5", "8", "3", "3"], 
        "Weapons": ["Pump Shotguns", "AK-47s", "Revolvers", "Sniper Rifles"],
        "Locations": ["Tilted Towers", "Greasy Grove", "Pleasant Park", "Flush Factory"],
        "Distance Away": ["1km", "2km", "3km", "4km"]}

table = pd.DataFrame.from_dict(data)

queries = ["Where are the enemies at?"]

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
    print(query)
    if predicted_agg == "NONE":
        print("Predicted answer: " + answer)
    else:
        print("Predicted answer: " + predicted_agg + " > " + answer)