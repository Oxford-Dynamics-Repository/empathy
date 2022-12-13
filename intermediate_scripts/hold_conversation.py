# Lucy Jackson (lucy@oxdynamics.com) - Oxford Dynamics - November 2022
# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics -November 2022
#
# This script is used to generate the input knowledge for the Seeker model.
# It draws answers from a database using TAPAS.

from transformers import TapasTokenizer, TapasForQuestionAnswering
import pandas as pd


class HoldConversation:
    def __init__(self):
        model_name = "google/tapas-base-finetuned-wtq"
        self.tapas_model = TapasForQuestionAnswering.from_pretrained(model_name)
        self.tapas_tokenizer = TapasTokenizer.from_pretrained(model_name)

        self.table = self.return_database()
        print(self.table)

    def get_keywords(self, query, model, tokenizer, table):
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
                return(answer, predicted_answer_coordinates)
            else:
                return(answer, predicted_answer_coordinates)
                
    def return_database(self):
        threat_info = {'threats':["5 enemies"], 'distance away from you':["5 minutes"],'weapons':["AK47s"], 'location':["Coverton Road"], 'wearing':["red jumpers"]}
        other_info = {'civilians':["Children"], 'location':["Regents Road"], 'distance away from you':["1 minute"], 'wearing':["blue coats"]}
        vehicle_info = {'cars': ["Black Ford Transits"], 'location':["Adams Court"], 'distance away from you':["30 minutes"]}
        base_camp = {'places':["Military Base"], 'location':["High Fields"], 'distance away from you':["7 minute"]}
        
        threat_info = pd.DataFrame.from_dict(threat_info)
        other_info = pd.DataFrame.from_dict(other_info)
        vehicle_info = pd.DataFrame.from_dict(vehicle_info)
        base_info = pd.DataFrame.from_dict(base_camp)
        
        table = pd.concat([threat_info, other_info, vehicle_info, base_info], ignore_index=True)
        table = table.fillna('N/A')

        return table

    def generate(self, output, coordinates, table):
        if table.iloc[coordinates[0][0][0],:][0] != "N/A":
            outer = table.iloc[coordinates[0][0][0],:][0]
        elif table.iloc[coordinates[0][0][0],:][5] != "N/A":
            outer = table.iloc[coordinates[0][0][0],:][5]
        elif table.iloc[coordinates[0][0][0],:][6] != "N/A":
            outer = table.iloc[coordinates[0][0][0],:][6]
        else:
            outer = table.iloc[coordinates[0][0][0],:][7]

        if coordinates[0][0][1] == 0: # threats
            response = f'There are {output} around.'
        if coordinates[0][0][1] == 1: # distance
            response = f'The {outer} are {output} away.'
        if coordinates[0][0][1] == 2: # weapons
            response = f'The {outer} are armed with {output}.'
        if coordinates[0][0][1] == 3: # location
            response = f'The {outer} are on {output}.'
        if coordinates[0][0][1] == 4: # wearing
            response = f'The {outer} are wearing {output}.'
        if coordinates[0][0][1] == 5: # civilians
            response = f'There are {output}.'
        if coordinates[0][0][1] == 6: # vehicles  
            response = f'There are {output} around.'
        if coordinates[0][0][1] == 7: # places
            response = f'There is a {output}.'
        return response

    def generate_seeker_input(self, question):
        question = question.replace(' vehicles', ' cars') # exception
        knowledge_input, coordinates = self.get_keywords(question, self.tapas_model, self.tapas_tokenizer, self.table)

        try:
            response = self.generate(knowledge_input, coordinates, self.table)
        except:
            response = 'no knowledge'
        
        return response


def main():
    ConversationObject = HoldConversation()
    print(ConversationObject.generate_seeker_input("Is there a military base?"))


if __name__ == '__main__':
    main()
