# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - December 2022
#
# This script uses the DistilGPT2 model form Huggingface. 

from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset


def finetune_model(model_checkpoint):
    # Defining the tokenizer function for the dataset mapping.
    def tokenize_function(examples):
        tokenizer.pad_token = tokenizer.eos_token
        return tokenizer(examples['text'], padding = True, truncation = True)
    
    # Adding labels to the features. 
    def add_labels(examples):
        examples['labels'] = examples['input_ids']
        return examples

    model_name = model_checkpoint.split('/')[-1]

    # Defining the tokenizer and model. 
    model = AutoModelForCausalLM.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

    # Loading the training and validation dataset.
    datasets = load_dataset('text', 
        data_files={'train': '../../dataset/IMDB/harry_potter_1_reviews_train.csv',
            'validation': '../../dataset/IMDB/harry_potter_1_reviews_val.csv'})

    # Applying the tokenizer to the dataset.
    tokenized_datasets = datasets.map(tokenize_function, batched=True, remove_columns=['text'])
    tokenized_datasets = tokenized_datasets.map(add_labels, batched = True)

    # Defining the training arguments.
    training_args = TrainingArguments(
        f'{model_name}-finetuned',
        evaluation_strategy = 'epoch',
        learning_rate=2e-5,
        weight_decay=0.01,
        num_train_epochs = 10,
        per_device_eval_batch_size = 1,
        per_device_train_batch_size = 1)

    # Defining the trainer object.
    trainer = Trainer(
        model = model,
        args = training_args,
        train_dataset = tokenized_datasets['train'],
        eval_dataset = tokenized_datasets['validation'])

    trainer.train()

def main():
    model_checkpoint = 'distilgpt2'
    finetune_model(model_checkpoint)
    

if __name__ == '__main__':
    main()