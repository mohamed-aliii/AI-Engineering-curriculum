import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# -----------------------------------------------------
# IMPLEMENTATION: Zero-Shot Classification & Retrieval
# -----------------------------------------------------
class DummyCLIP(nn.Module):
    def __init__(self, patch_size=16, img_size=224, d_out=512, txt_vocab=128):
        super().__init__()
        n_patches = (img_size // patch_size) ** 2  # = 196
        patch_dim = 3 * patch_size * patch_size    # = 768
        # Image encoder: patches -> embedding (simplified ViT)
        self.patch_embed = nn.Linear(patch_dim, d_out)
        self.cls_token = nn.Parameter(torch.randn(1, 1, d_out))
        self.img_proj = nn.Linear(d_out, d_out)
        # Text encoder: token sequence -> embedding (simplified)
        self.txt_embed = nn.Embedding(txt_vocab, d_out)
        self.txt_proj = nn.Linear(d_out, d_out)
        self.logit_scale = nn.Parameter(torch.ones([]) * np.log(1/0.07))
    
    def encode_image(self, x):
        # x: [B, 3, H, W] → patchify → [B, N, patch_dim]
        B, C, H, W = x.shape
        p = 16
        x = x.reshape(B, C, H//p, p, W//p, p).permute(0,2,4,1,3,5)
        x = x.reshape(B, -1, C*p*p)  # [B, 196, 768]
        x = self.patch_embed(x).mean(dim=1)  # Average pool patches
        return F.normalize(self.img_proj(x), dim=-1)
    
    def encode_text(self, t):
        # t: [B, seq_len] integer token indices
        x = self.txt_embed(t).mean(dim=1)
        return F.normalize(self.txt_proj(x), dim=-1)
    
    def forward(self, images, text_tokens):
        img_feat = self.encode_image(images)
        txt_feat = self.encode_text(text_tokens)
        scale = self.logit_scale.exp()
        return scale * img_feat @ txt_feat.T, scale * txt_feat @ img_feat.T

# TEST IT
model = DummyCLIP()
images = torch.randn(3, 3, 224, 224)
text_tokens = torch.randint(0, 128, (5, 20))  # 5 captions, 20 tokens each
logits_i2t, logits_t2i = model(images, text_tokens)
assert logits_i2t.shape == (3, 5), f"Expected (3,5), got {logits_i2t.shape}"
assert logits_t2i.shape == (5, 3), f"Expected (5,3), got {logits_t2i.shape}"

# 1. Zero-Shot Classification: Given an image, which text describes it best?
probs = logits_i2t.softmax(dim=-1) # shape: [3 images, 5 potential labels]
predicted_labels = probs.argmax(dim=-1)
print(f"Zero-Shot Classification - Given 3 images, the predicted label IDs are: {predicted_labels.tolist()}")

# 2. Zero-Shot Retrieval: Given Text Query #2, which image is it?
text_query_idx = 2
image_retrieval_probs = logits_i2t[:, text_query_idx].softmax(dim=0) # [3 potential images]
best_image_match = image_retrieval_probs.argmax().item()
print(f"Zero-Shot Retrieval - Given text query '{text_query_idx}', Image #{best_image_match} is the closest match.")