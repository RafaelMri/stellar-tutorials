title: Quorum slices and the quorum function
date: 2013-07-15 12:00:00
order: 1

# Understanding the Stellar protocol: quorum slices and the quorum function

_In this post, we explain how Stellar reaches network-wide consensus using quorum slices. We go over 2 key ideas, quorum slices and the quorum function, which are not cryptographic in nature but set-theoretic, using [Python](https://www.python.org/)._

A key technical innovation of the Stellar protocol is the introduction of __federated Byzantine agreements__. These allow 4 cool things:

1. To reach consensus __fast__ and __cheaply__: within a few seconds and spending little energy
2. To let __anyone join__ the consensus process: no one has all the decision-making power
3. To let everyone __decide who to trust__: if you want to be trusted, you better play clean
4. To be __safe__: even if bad actors join the network, the network can still reach the "right" consensus

All of this rests on 2 key ideas: __quorum slices__ and the __quorum function__. The good news is that these depend mostly on [__set theory__](https://en.wikipedia.org/wiki/Set_theory)!

<!-- ## I don't like reading, give me the example already!

[APP]

This app provides a playground to experiment with the idea of nodes, quorum slices, and quorum. To see what all of this means, read the rest of the article!
 -->
## A network of nodes

__Quorum slices__ and the __quorum function__ make no sense in isolation; they need _context_. This context is the __network of nodes__.

Let's say we have 3 people: `Alice`, `Bob`, and `Charlie`. They're trying to decide what movie to watch. They will be our __network of nodes__. Abstractly, we can stuff them all into a set called `friends`.

    friends  = {'Alice', 'Bob', 'Charlie'}  # This is a set!
    print(friends)

In mathematics, every [set](https://en.wikipedia.org/wiki/Set_(mathematics)) has associated to it another set, called its [__powerset__](https://en.wikipedia.org/wiki/Power_set). In Python, we can build powersets like this:

    def powerset(s):
        """This function builds powersets. It takes a set `s` and returns the powerset of `s`.
        The powerset contains all subsets!"""

        n = len(s)  # Size of our set
        s = list(s)  # We turn our set into a list to allow indexing

        subsets = []  # Our powerset will actually be a Python list, for simplicity
        for i in range(2**n):  # We loop through each of the 2**n subsets of our set
            subset = {s[j] for j in range(n) if (i & (2**j))}
            subsets.append(subset)

        # We sort the powerset (actually a Python list) by length!
        # This is simply to aid visualization.
        return sorted(subsets, key=lambda x: len(x))


    friends  = {'Alice', 'Bob', 'Charlie'}  # This is a set!
    powerset_friends = powerset(friends)
    print('set: ', friends)
    print('powerset: ', powerset_friends)

You can run this snippet here:

<iframe src="https://trinket.io/embed/python3/e9154c20ae?toggleCode=true&runOption=run&start=result" width="100%" height="180" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Notice the set `friends` has 3 elements, and its powerset has 8 elements. This is no coincidence. In general, a set with `n` elements yields a powerset with `2**n` elements. In Python, `set()` stands for the set containing no elements at all, called the __empty set__. The powerset of `friends` contains every possible [combination](https://en.wikipedia.org/wiki/Combination) of `friends`, including the "empty" combination!

## A quorum slice: just a set of nodes... with a twist

Now that we have a set and and its powerset, we can start building __quorum slices__.

Each person in our example is a __node__. The set of all nodes is the __network__. A __quorum slice__ is a subset of the network. A quorum slice doesn't make sense by itself; it needs to be associated to a node. So we'll be talking about "a quorum slice for `Bob`", or "a quorum slice for `Alice`".

Neglecting details, a quorum slice for `Alice` is just a __set of nodes__ containing `Alice`.

Here's an example of a possible quorum slice for `Alice`:

1. __NODE__: `Alice`
2. __POSSIBLE QUORUM SLICE FOR `Alice`__: `{Alice, Charlie}`

Here's an example of an _impossible_ quorum slice for `Alice`:

1. __NODE__: `Alice`
2. __IMPOSSIBLE QUORUM SLICE FOR `Alice`__: `{Charlie, Bob}`

It's impossible because it doesn't contain `Alice`!

Notice a quorum slice for `Alice` is just some __element of the powerset__. Of course, not every element of the upowerset _needs_ to be a quorum slice for `Alice`. Also, some elements of the powerset _can't_ be quorum slices for `Alice`.

And here comes the _twist_. If `Alice` wants some set of nodes to be her quorum slice, that set of nodes must satisfy an additional property: __it must be trusted by Alice__. Put another way: _Alice must trust her quorum slice_.

__Trust__ is a very strong word: a set of nodes that `Alice` trusts can influence her decisions!

One of the key properties of federated Byzantine agreements is that _every node decides which nodes it trusts_. Or, to use our new language: __every node chooses its quorum slice__.

But that's not all. The last detail is: `Alice` isn't limited to a single quorum slice. __She can choose as many quorum slices as she likes__!

I like to refer to all of `Alice`'s quorum slices as `Alice`'s "happy family".

__Question__. What is the largest possible quorum slice for `Alice`?  
__Answer__. `{Bob, Charlie, Alice}`.  

__Question__. What is the smallest possible quorum slice for `Alice`?  
__Answer__. `{Alice}`, meaning `Alice` trusts no one but herself.  

__Question__. What are _all_ the possible quorum slices for `Alice`?  
__Answer__. There's 4 possible quorum slices:  

1. `{Alice}`
2. `{Bob, Alice}`
3. `{Charlie, Alice}`
4. `{Bob', Charlie, Alice}`

__Question__. What is the largest possible "happy family" for `Alice`?  
__Answer__. `{ {Alice}, {Bob, Alice}, {Charlie, Alice}, {Bob, Charlie, Alice} }`, which is every quorum slice possible.  

__Question__. What is the smallest possible "happy family" for `Alice`?  
__Answer__. The smallest "happy family" for `Alice` has 1 quorum slice. There's 4 such "happy families":

1. `{ {Alice} }`
2. `{ {Bob, Alice} }`
3. `{ {Charlie, Alice} }`
4. `{ {Bob', Charlie, Alice} }`

## The quorum function: each node has a family of quorum slices

`Alice` can choose as many quorum slices as she likes. So, `Alice`'s "happy family" can have 1, 2, 3, or 4 members.

<!-- [APP. Alice's happy family] -->

The __quorum function__ says which particular family of quorum slices `Alice` chose. The quorum function doesn't work only on `Alice`, though, but on every node!

And that's all the quorum function is: _the object that contains all the information about which particular "happy family" each node chose_.

If we call the quorum function \( \textbf{Q} \), then we can refer to `Alice`'s "happy family" as \( \textbf{Q}(\text{Alice}) \).
More formally, \( \textbf{Q}(\text{Alice}) \) is _the value of the quorum function evaluated at `Alice`_.

## Federated Byzantine agreement systems (FBAS)

A __federated Byzantine agreement system__ (FBAS, for short) is simply a network of nodes together which a particular quorum function.

The [SCP white paper](https://www.stellar.org/papers/stellar-consensus-protocol.pdf) puts it like this:

__Definition (FBAS)__. A federated Byzantine agreement system, or __FBAS__, is a pair \( (\textbf{V}, \textbf{Q}) \) comprising a set of nodes \( \textbf{V} \) and a quorum function \( \textbf{Q} : \textbf{V} \longrightarrow 2^{2^\textbf{V}} \backslash \{\emptyset\} \) specifying one or more quorum slices for each node, where a node belongs to all of its own quorum slices.


In set-theoretic terms, the "happy family" is __an element of the powerset of the powerset__.


And now we're ready to define the __quorum function__. The quorum function is simply an assignment of nodes to quorum slices.

The __quorum function__ says each node must have a family of trusted nodes.

Of course, since every node chooses its own quorum slices (its "happy family")

<!-- Eg. if `A`

[APP]
 -->
But that's not the whole story! Each node isn't limited to just _one_ such family; it can choose as many as it wants!


Of course, a network of nodes can have many, many quorum functions. A particular quorum function simply corresponds to a particular assignment of quorum slices.


<!-- All of this talk of talk of sets, powersets, slices, etc., allows us to understand the definition in the SCP white paper: -->


## Can we watch the movie already?

Remember this whole nightmare started when the 3 friends decided to watch a movie.

We've still got a bit of ground to cover before we're ready for that. After going over __quorums__, __federated voting__, and __the ballot process__, we'll finally be ready. Stay tuned for __part 3__.


<!-- ## Quorums


Unlike quorum slices, quorums do make sense by themselves: a quorum is not associated to any node in particular. Rather, quorums are associated to a network after we choose a particular quorum function!

Here's an example of a quorum slice in our network:

1. __NODE__: `Alice`
2. __QUORUM SLICE FOR `Alice`__: `Alice`, `Charlie`

Here's an example of an _impossible_ quorum slice for `Alice`:

1. __NODE__: `Alice`
2. __QUORUM SLICE FOR `Alice`__: `Charlie, Bob`


__Question__. Under this quorum function: 


, what's the smallest quorum containing `Alice`?  
__Answer__.

## Quorum intersection: Don't leave the house without it!

__Quorum__ doesn't _not_ mean network-wide consensus! Imagine this scenario:

[...]

Here, `A` and `B` have quorum, and `C` has quorum, but there's no __network-wide consensus__!

This situation is so critical to federated Byzantine agreements that it gives rise to a name: __quorum intercetion__. In this particular example, our network does _not_ have __quorum intersection__, and so it can never agree on anything!

If a network has agreed on something, then we know it must have quorum intersection. If, however, it has quorum intersection, then it may or may not agree on anything!

__Quorum intersection__ is property has takes a bit of effort to visualize, because it involves _every single quorum in the network_. And each quorum in the network involves a bunch of quorum slices, which in turn involve a bunch of nodes.

So let's start with the simplest case: no quorum at all.

Then: 1 quorum.

Then: 2 quorums.

Then: 3 quorums.

An _algorithm_ to determine whether a network has (or doesn't have) quorum intersection would be:

1. Find all quorums the network.
2. Construct a list of all __pairs__ of quorums.
3. Find the intersection each pair in that list.
4. If _each_ intersection is not empty, then your network has __quorum intersection__. Otherwise, it doesn't!

Example in Python:

```python
```

__Quorum intersection__ is needed for network-wide consensus because, without it, disjoint quorums can agree an different things! Disjoint quorums effectively function as two distinct federated Byzantine agreement systems, and each may follow its own path, unbeknown to the other.

## Federated voting: vote, accept, ratify, confirm

But we're not ready for consensus just yet. First we must go through a __federated voting__ process, which has 4 steps: vote, accept, ratify, confirm.

## The ballot process

But that's not the end of our woes. 

 -->