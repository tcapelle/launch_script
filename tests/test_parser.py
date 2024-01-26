from wandbize.parser import parse_command


def test_cmd_parser():

    cmd = """
    accelerate launch -m lm_eval \
        --model hf \
        --model_args "pretrained/merged/,load_in_4bit=True,use_cache=True,attn_implementation="flash_attention_2",trust_remote_code=True" \
        --tasks hellaswag,arc_challenge,mmlu,truthfulqa,winogrande,gsm8k \
        --batch_size 1 \
        --output_path "/home/ubuntu/cape/eval_harness_outputs"
    """

    args, kwargs = parse_command(cmd)
    assert args == ['accelerate', 'launch', '-m', 'lm_eval']
    assert kwargs == {
        'model': 'hf',
        'model_args': 'pretrained/merged/,load_in_4bit=True,use_cache=True,attn_implementation=flash_attention_2,trust_remote_code=True',
        'tasks': 'hellaswag,arc_challenge,mmlu,truthfulqa,winogrande,gsm8k',
        'batch_size': '1',
        'output_path': '/home/ubuntu/cape/eval_harness_outputs'
    }