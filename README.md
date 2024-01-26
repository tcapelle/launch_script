# Wandbize

Your tool to transform any script into a wandb compatible script!

## Usage

```bash
wandbize --cmd="python train.py --batch_size=32 --epochs=10 --output='out.txt'" \ 
    --project="my_project" \
    --entity="my_entity" \
    --output='out.txt' \
    --log=True
```
