from fastapi import FastAPI, UploadFile, File
from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import re

app = FastAPI()

# Load model and processor once on startup
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2").to(device)

@app.post("/extract")
async def extract_receipt(file: UploadFile = File(...)):
    # Load image
    image = Image.open(file.file).convert("RGB")
    
    # Prepare input
    pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)
    task_prompt = "<s_cord-v2>"
    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids.to(device)

    # Generate
    outputs = model.generate(
        pixel_values,
        decoder_input_ids=decoder_input_ids,
        max_length=model.config.decoder.max_position_embeddings,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        return_dict_in_generate=True,
    )

    # Decode and format to JSON
    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
    sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()
    
    return processor.token2json(sequence)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)