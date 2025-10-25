# Case #75 - [PyTorch] torch.vmap

> 🧩 Reference: [LinkedIn Post](https://www.linkedin.com/posts/backnumber19lim_pytorch-ai-ml-activity-7363130990283689984-J3ER?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC4i7ZsBMeUAH3UpBvhusYv1qkmTlPJ4E6E)  

Vectorization is a technique that eliminates loops and performs operations on entire datasets at once. vmap (vectorized map) is a tool that makes it easy to apply vectorization even to complex or user-defined functions.

vmap originated from JAX and was introduced to PyTorch through the functorch library. However, this feature proved so useful that it was integrated directly into PyTorch core starting from version 2.0. Therefore, torch.vmap is now recommended over functorch.vmap.

vmap is useful in all situations where the same operation needs to be applied independently to each sample in a batch. In AI/ML, it's primarily used for per-sample gradient computation and ensemble model processing. However, it may not be suitable for cases requiring inter-sample interactions, such as RNNs or Attention mechanisms.

The example below compares the speed difference between traditional loops and vmap. Using a simple mathematical function implemented as a model, we measured computation time across different randomly generated data sizes. You can see that vmap's speed improvement becomes more pronounced as data size increases.

⚠️ When processing large batches, memory shortage may occur. In such cases, you can use the chunk_size parameter of torch.vmap to process batches in chunks of the specified size.

![vmap Implementation and Results](https://media.licdn.com/dms/image/v2/D5622AQH1Bo-nlLAYSg/feedshare-shrink_800/B56Zi8Ym2QHQAk-/0/1755507225464?e=1762387200&v=beta&t=7x1E0K5TCWcat7LvOrX-f-JanVbelxfbbhX4mNzid-w)