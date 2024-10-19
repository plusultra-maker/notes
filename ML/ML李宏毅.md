# 李宏毅ML 2021/2022 notes

## CNN
### course
key points:
kernel size, padding, filters, pooling, MLP in the end
提到了很有意思的一件事，就是AlphaGo是用CNN做的，做成了一个分类问题，但它又用了类似RL的蒙特卡洛搜索，这是怎么结合起来的
A:CNN的工作仅仅是创造更多更合适的“逻辑”来建立一个从state到action的决策结构，而蒙特卡洛搜索是说我怎么评价这个action到底好不好，其实是个延续的过程

## self-attention & transformer
### course
done
### lab

## BERT
### course
done
### lab

## GAN
### course
#### basic discussion
- generative model: 
  - input: x, z from simple distribution p(z)(z is a random variable)
  - output: y (from complex distribution p(y) in theory)
- why generator:
  - the right output (from training data) is not certain
  - the answer should be a distribution ---- creative
- input distribution: 
  - simple distribution p(z)-- normal distribution is good enough
  - the generator will learn to map z to y, which is complex
  - z can vary continuously, so the output y can vary continuously
- Network:
  - generator: z -> G -> y
  - discriminator: y -> D -> 0/1 ( or regression like -1~1)
  - 非常重要的是，generator+discriminator实际上是一个连续的大网络，只是在训练的时候分开训练，因此generator的训练中梯度是从discriminator那边传过来的
- Training:
  - generator 1 time (random sampled input z), loss = -log(D(G(z)))
  - discriminator 1 time, loss = -log(D(y)) - log(1-D(G(z)))
- math theory:
  - $$G* = argmin_G Div(p_{data}||p_g)$$
    - but divergence is hard to compute, we don't know p_g and p_data
    - but we can sample from each, then train a discriminator to use a regression loss to represent the divergence
  - why or how will the discriminator be trained to be a good estimator of the divergence?
    - D is trained to maximize the probability of assigning the right label to the right data aka $$ D*=argmax_D E_{x\sim p_{data}}[log(D(x))] + E_{z\sim p_z}[log(1-D(G(z)))]$$
    - This binary classification object function (if optimized) is related to the Jensen-Shannon divergence between p_data and p_g (see the original paper)
  - Divergence types & related object functions:
    - see FGAN paper
- Difficult to train:
  - JSD is always log2 when P_G and P_data are disjoint, so the gradient will be lost
    - since P_G and P_data are low-dimensional, they may easily be disjoint
    - also low sample density may cause the D to be too easy to distinguish with 100% accuracy -- lose gradient 
    - Training GAN may lose its way in the early stage
  - WGAN: Wasserstein GAN
    - W distance: the minimum cost of transforming one distribution to another(distances between two distributions), always have a gradient
    - then the object function of D is:
    $$D* = argmax_D E_{x\sim p_{data}}[D(x)] - E_{z\sim p_z}[D(G(z))]$$
    D belongs to 1-Lipschitz, meaning to be smooth enough (not too sharp)
    - but how to train this D to meet the condition?
      - gradient clipping
      - gradient penalty
    - lose of gradient when generator contains discrete function
      - e.g. generate a sentence (character) using classifier, changing a bit on the generater may not change the output
  - Evaluation of Generater:
    - off-the-shelf evaluation: a out-of-the-box classifier to evaluate if the generated data's distribution is concentrated enough--meaning the output is certain enough
    - Mode Collapse: 
      - the generator may only generate a few samples inside the data distribution, meaning the output distribution is a very small (seemingly discrete) subset of the data distribution
      - so far no good solution-- but model collapse is a process during training, so we can monitor it and stop the training when it begins to collapse
      - easy to detect, we can see the output may repeat itself (even from various z)
    - Model Dropping:
      - just like model collapse, but the output is not repeated, but falls into a subset of the data distribution
      - it could lead to that, some features are too concentrated, like the color of the generated faces
- Conditional GAN:
  - input z is still random, but we add a condition x to the generator to direct the output
    - so the x will decide the output distribution, and z still decides the randomness
  - therefore, we need discriminator to be conditioned on x as well, so will need labels(as condition) and data as pairs to train the discriminator
    - need right paired data to be signed as 1, and also need fake data including which the output is wrong and which the input label does not match the output as 0
  - the point is use label to generate, but still maintain the randomness
    - text-to-image, abstract image to concrete image, voice to image, etc.
- Cycle Gan:
  - First, Cycle GAN is not a conditional GAN, the input is not a condition, but an image, which can be seen as a sample from A-type image distribution. So this image plays the role of z in a normal GAN
    - recall the part we said z can be any random variable, we used normal distribution just because it is easy to sample from. So here, the input image is a sample from A-type image distribution, and the output should be a sample from B-type image distribution
  - But what's more, we need to ensure the output is corresponding sample from input (we don't need any correspondence in normal GAN since z has no meaning)
    - so we need to add a cycle consistency loss to ensure the output of the generator can be mapped back to the input (which means the output somehow contains the input information)
    - so two generators are needed (map forward, map backward), and one discriminator to evaluate the output is close to B-type image distribution, and the cycle consistency loss is added to ensure the output can be mapped back to the input
  - Apparently there should be a lot of possible solution to these constraints, these constraints are not a definition of the correspondence
    - But in practice, the network can work because it is always too lazy to change the input too much, so the output will have the correspondence that we want (if what we want is reasonable)
#### To learn more
- math on goal of GAN
  - Maximum Likelihood Estimation
    - $$\theta* = argmax_{\theta} \prod_{i=1}^{n} p_{G}(x_i; \theta)$$
    - MLE is to find the parameter that maximizes the probability of the data (samples from the desired distribution)
  - MLE = Minimize KL divergence
    - $$\theta* = argmin_{\theta} KL(p_{data}||p_{G})$$ 即最小化 log p_data - log p_G在data分布上的期望
    - KL divergence is the difference between two distributions, so MLE is to minimize the difference between the generated distribution and the data distribution
  - back to GAN
    - $$max_D V(G, D) =-2log2 + 2JSD(p_data, p_g)$$
    - $$JSD(p_data, p_g) = KL(p_data||\frac{p_data+p_g}{2}) + KL(p_g||\frac{p_data+p_g}{2})$$
    - So JSD is just like the KL divergence, but with a symmetric form
- math on training
  - the training is alternating between G and D
  - it works locally, because we believe we should train D to be a good estimator of the divergence, and then train G a little bit to make the divergence smaller (but in practice, it doesn't work this way)
- Model collapse
  - the possible reason is that for specific divergence type, maybe we will fall into a local probability high-density area, and the generator will only generate samples from this area
## Autoencoder
### course
done
- (plus) VAE
  - 用中文好了
  - 简单来说就是autoencoder的基本思路还是想要的数据是一个高维空间中的低维流形，因此将输入映射到一个低维空间，然后如果可以映射回来，就说明这个低维空间是一个合理的压缩
  - 问题在于纯训一个autoencoder，可能会导致缺少一些随机性，映射是确定的，而数据是离散的，因此训练得到的latent space没有能连续的理解一个低维，而是一些离散的对应
  - 因此，我们希望用一定的分布来描述encode和decode的过程，这样一定程度加强了随机性，使得latent space更连续
  - 从数学上看，我们的根本目标就是用网络来学习数据的分布P(x)，因此目标是优化MLE即P(x)在data上的求和，而我们对P(x)的表达可以借助latent space中采样的z来实现。不妨令latent space是一个normal distribution, 而从latent space中采样z，由z经过nn得到一个u和sigma，再用u和sigma采样得到x，这样我们就可以用z的一个nn来表达了P(x)，即Guassian model estimator.那么省去一些推导，max P(x) 就变成了 最小化 P(z|x)与P(z)的KL divergence，以及最大化 $E_{z~P(z|x)}[P(x|z)]$，这两个目标就是VAE的目标。 而第一个就是loss function中 regularize项的来源，第二个就是loss function中的reconstruction loss的来源
    - 这里有点问题，为什么我们能假定P(z)是一个normal distribution。实际是z是一个我们假象的latent sample，它的作用是进入decoder得到一个新的x；而data进入encoder得到的z_en不代表z的分布，我们只是认为z_en是latent space中的一个点，而与z的固有分布无关。因此，我们只是假设z是一个normal distribution，而不是说z_en是一个normal distribution。实际上P(z)是一个normal distribution是为了让z能够连续且便于新的采样。而P(z|x)与P(z)的KL divergence是为了让从x经过encoder得到的z_en更接近一个合理的z的采样，就像我们希望x'是一个合理的x的采样一样。x和z从数学上没有什么差别。
  - VAE的问题：
    - VAE是在模仿数据，某种插值，而其生成性不显著（从数学上怎么理解？）
    - __！！！！！！！！TODO__：如何理解VAE的生成性不显著
- (plus) Flow-based model
### lab