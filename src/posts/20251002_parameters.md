---
date: 2025-10-02
title: What even is a "parameter"?
categories:
- Statistics
tags:
- explainer
authors:
- etosch
---

"Parameter" is one of those commonly used words in mathematics and computing and in my experience is rarely explicitly defined. While most uses have similar meanings, there can be small differences in their interpretation. Parameters and other statistical entities are important to the semantics and correctness of the Helical system, so it's worth considering what we mean by these terms.

## OED Definitions

Let's start by taking a look at how the Oxford English Dictionary defines "parameter". 

### Regular old mathematics

Under the entry for mathematics we have two definitions:

> A quantity which is fixed (as distinct from the ordinary variables) in a particular case considered, but which may vary in different cases; esp. a constant occurring in the equation of a curve or surface, by the variation of which the equation is made to represent a family of such curves or surfaces (cf. quot. 1816 at sense I.1). Also (Computing): a quantity whose value is specified when a routine is to be performed. (1833-)

<p></p>
> An independent variable in terms of which each coordinate of a point of a curve, surface, etc., is expressed, independently of the other coordinates. (1855–)

These two definitions track with what I'd guess is most people's first exposure to parameters, in physics. For example, let's consider Hook's law: $F = kx$. Here $F$ represents force, $k$ is a spring constant, and $x$ is distance. The parameter is "fixed...in a particular case considered": i.e., there is only one value of $k$ for each spring. To make this relationship very clear, we might instead express Hook's law using the notation: $F_s = k_s x$ to indicate that _this_ $k$ is the spring constant for _this_ spring (called $s$) and that $F_s$ is the force required to stretch $s$ $x$ units of distance. 

If we wanted to make it clear that the parameter $k$ can be thought of as a special kind of input, we might alternatively write Hook's law as $F(x; k) = k x$. Here we are using the semicolon (rather than comma) to indicate that there is a qualitative and semantic distinction between these two inputs. 
 
We can also think about Hook's law as a higher-order function $F : S \rightarrow \mathcal{R} \rightarrow \mathcal{R}$ where $S$ is the domain of springs or the domain of numeric spring identifiers, or something similar. We would apply $F$ to our spring of interest and get a unary function that has instantiated and fixed the spring constant. Note that in this context, $k_s$ is the parameter, not $s$. 

Parameters specialize functions in some way; we often say that a parameter "indexes into" a "family" of functions.[^1] What this example also illustrates is that the need to refer to a term in an equation as a "parameter" in many situations is a proxy for scope (especially in contexts where we don't 
really have a notion of scope). We expressed scope above using a higher order function, but we could just as well have used a let binding, arguments to a command line program, or another mechanism for specializing computation. 


### Statistics

Under the entry for statistics we have:

> A numerical characteristic of a population, as distinguished from a statistic obtained by sampling. (1920-)

The first set of definitions make no mention of the domain, nor the semantics of the parameter. Statistics narrows the scope considerably. 

## Parameters in Statistics vs. Probability

First a refresher on how statistics differs from probability theory: a _statistic_ is any function of data[^2] and so the study of statistics is the study of functions of data. Probability theory is the formal study of the properties of stochastic phenomena. One way to think about their relationship to each other is that probability theory provides a language for describing the ground truth of stochastic phenomena, while statistics provides a language of relations over data. 

It is important to distinguish between _parametric distributions_ and _parameterized models_ or _parametric statistics_.

### Parameters in Probability Theory

In probability theory, a distribution may be parametric or non-parametric. It can be easier to define a non-parametric distribution first, but to do so, we need to recall some basic defintions.

#### Non-Parametric Distributions

Most introductions to probability theory I've seen begin with a set-theoretic treatment of the _sample space_ where we assign _probabilities_ to _events_ (i.e., subsets of the sample space). The function that assigns these probabilities must obey certain axioms for its to be a well-formed probability function. When events can be meaningfully assigned numeric values, we say that the map from events to numbers is a _random variable_ and that the mapping from those numbers to probabilites is its distribution (i.e., a probability function for random variables).  We typically denote a random variable with a capital Roman letter.

We typically choose to use random variables instead of events when the _probabilistic queries_ we want to ask are with respect to the random variable's codomain. That is, when we write $P(X = n)$ (what is the probability that $X$ is $n$?), this statement should be understood to mean $\sum_{\lbrace e \mid e \subseteq \Omega \wedge X(e) = n \rbrace}f_\Omega(e)$, where $f$ is the mass or density function associated with the underlying sample space. 

<!-- and ask _probability queries_ with respect to its codomain using the notation $P(X(e) = n)$ to mean "what is the probability that event $e$ has value $n$?  Unless it is contextually important, we generally omit the event and simply write $P(X = n)$ ("what is the probability ) -->

When the number of the coefficients of the terms of the functional form of $f$ is _not_ strictly less than the size of the sample space[^3] minus one, then we say the distribution is non-parametric.[^4] Symbolically, if we let $\Theta$ represent the parameters, then when $\Theta < \Omega - 1$, the distribution is parametric. One consequence of this definition is that any finite sample space can be represented by a parametric distribution because in the worst-case scenario, we need $|\Omega| - 1$ parameters for the first $|\Omega| - 1$ elements of the sample space; the mass associated with the last element must be one minus the sum of the parameters (i.e., it is no longer free to vary). 

Because $\infty - 1 \equiv \infty$, discrete sample spaces of infinite size are non-parametric. We would need to look to more sophsticated probabilistic process models in order to 
encounter such a distribution; they are out of scope for this already-too-long post, but for interested readers, one such example is the [Chinese Restaurant Process](https://en.wikipedia.org/wiki/Chinese_restaurant_process). Critically, such distributions may have terms we refer to as "parameters" but they are _non-parametric_ distributions; the "parameters" of these mathematical objects are parameters in the traditional mathematical sense, not in the probability-specific sense.

#### Parametric Distributions

Parametric distributions are what you typically learn in an introduction to probability theory: e.g., Categorial, Binomial, and Normal distributions. One particularly useful aspect of parametric distributions is that you can compute the probability of any event knowing only the parameters. 

The parameters of parametric distributions typically have meaningful "real-world" interpretations. This is where they connect to statistics. 

### Parameters in Statistics

We can use statistics to answer questions about a single variable (_univariate_ models) and to answer questions about multiple variables (_multivariate_ or _associational_ models). One of the primary goals of statistics is to use the data we have now, that we have actually collected and observed in the world, to make _inferences_ about the general space of data in our domain of interest. 

#### Non-Parametric Statistics
Just like in non-parametric probability distributions, we could make the argument that there are parameters in the mathematical sense (e.g., coefficiences of a fitted curve), but the number needed to describe mass or density on a sample space may grow with the data. We may use non-parametric statistics to estimate data drawn from _either_ parametric or non-parametric distributions; there are valid reasons to pick one or another, but fundamentally parametricity of the underlying distribution of the dat does not _determine_ the statistical methods we use.

#### Parametric Statistics

In parametric statistics, we start with an assumed model family and data. 

When our model is univariate, the model corresponds to a probability distribution and the task is to estimate its parameters from data. For example, we might model the length of a six week old Beagle puppy as a Normal ($X\sim\mathcal{N}(\mu, \sigma^2)$) distribution. Given a large enough random sample of Beagle pupples, we can compute the sample average length; sample average is what's known as an _unbiased estimator_ for the parameter $\mu$ of a Normal distribution. 

You might infer inductively from the above paragraph that when our model is multivariate, we are seeking to model a joint probability distribution. However, that's typically not the case! Instead, the most commonly used multivariate model is _linear regression_, which has the form $Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_n X_n$. In order to make estimation tractable, most models assume a functional form for each $X_i$ such that all $X_i$ have equal variance to each other, e.g., $X_i \sim \mathcal{N}(\mu_i, \sigma^2)$. 

Critically, the "parameters" of this model are the coefficients $\beta_i$, _not_ $\mu_i$. While the $\mu_i$ are related to the coefficients we seek to estimate, they are _not_ the parameters that definie this parametric distribution. They are however weights that may be assigned sime kind of semantics related to summary information about the data.

## Final Notes

Because statistics as a field is definitionally about data, it is fundamentally empirical and thus based on observation of phenemena in the real world. These data are drawn from a population, hence the appearance of "population" in the OED's definition. We won't get deep in the weeds on what a "population" really is (that's for another blog post!); instead it's important to think about a "population" mapping abstractly to a space of data points and the parameter being a fundamentally unobserved mathematical object that defines that space. 

<!-- Now, this stataement mmay seem to evoke the so-called Bayesian vs. frequentist argument; for the uninitiated, this is a debate in the statistics community about when and how a statistical object can be treated as a random variable or random process. There are many interesting philosophical ramifications of this debate: for example, is uncertainty epistemic or aleatory and does that matter? The examples we care about in the Helical project are grounded in stochastic behavior and the unmodeled variability of a population; that is, the circumstances that led a Bayesian interpretation of probability do not apply here. I note the existence of the Bayesian perspective only to point out that Bayesian statistics also employs parameters, but their interpretation may differ. -->


[^1]: Without getting too ahead of myself, I'd argue that the language of "indexing into" a family of functions implies that after specialization, the resulting relation is a function, which is not necessarily true without additional assumptions and kind of the whole point of this and forthcoming blog posts. :)
[^2]: Unless otherwise noted, all defintions are from the textbook I used in my graduate course in fundamental statistics: _Statistical Inference_, 2nd edition, by Casella and Berger.
[^3]: I haven't actually seen or found any satisifying definitions of parametric vs. non-parametric distributions in a strict probability theory context in any of the reputable textbooks I've used; this seems to be one of those things that authors assume everyone understands. Therefore, what I'm presenting is my own understanding of the terminology from having taught this material several times. Please do drop me a line if my definition is either incorrect or if you are aware of an appropriate citation!
[^4]: We are defining parametricity in terms of a mass or density function $f$ on a sample space $\Omega$, but all of these arguments also apply in the case of a random variable $X$ and its _support_ $\mathcal{X}$. We do not get into the definition of a support here both because it is not especially relevant and because a proper definition for the continuous case requires a discusion of Borel spaces, which is getting quite far afield from what I wanted to focus on in this post!