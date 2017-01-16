title: Stellar for (blockchain) newbies
date: 2013-07-15 12:00:00
order: 0

# Stellar for (blockchain) newbies

_This is part 1 in a tutorial series on [Stellar](https://www.stellar.org/). Throughout the series we'll go over the theoretical ideas underpinning Stellar, and we'll learn to automate our interactions with the network using [Python](https://www.python.org/), through the Horizon REST API._

Stellar is a decentralized, federated financial platform with a native asset, the __lumen__. Why is Stellar is decentralized? Why is it federated? What is a lumen? We'll go through this step by step.

The __lumen__, like bitcoin, is a [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency). A cryptocurrency is a [currency](https://en.wikipedia.org/wiki/Currency) whose power/value stems not from the authority of a sovereign state, but from the principles of [mathematics](https://en.wikipedia.org/wiki/Mathematics) (more precisely, [number theory](https://en.wikipedia.org/wiki/Number_theory)).

__Blockchains__ are at the heart of cryptocurrencies. __Consensus__ is at the heart of blockchains.

In one sentence, a __blockchain__ is a __distributed ledger__.

A __ledger__ is just a sequence of transactions. The ledger keeps a record of every transaction ever made, and everyone keeps a copy of that ledger. __Consensus__ is what makes the _"distributed"_ part work. Consensus on what, though? In Stellar's case, we must reach consensus on the __state of the Stellar network__. What is the Stellar network? What is its "state"? More on this later.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Hauptbuch_Hochstetter_vor_1828.jpg" alt="Ledger" style="width:100%; height:100%;">  
_A physical ledger from 1828. Wikipedia article on [ledgers](https://en.wikipedia.org/wiki/Ledger)._  

Stellar reaches consensus by turning __local consensus__ into __global consensus__. Local consensus is called a __quorum slice__. Global consensus is called __quorum__. Global consensus arises when there's enough local consensus in the network. Or, to use the new language: __quorum__ arises when there's enough __quorum slices__ in the network. The tricky part is to define __enough__.

The punchline in Stellar's consensus mechanism is: __global consensus doesn't need everyone to agree with everyone__. It's enough for everyone to simply __agree with their "neighbors"__, and, by having everyone __agreeing with a small neighborhood around them__, global agreement/consensus magically arises. Well, not magically, but mathematically.

The formal properties of Stellar's consensus algorithm allow 4 important things:

1. To reach consensus __fast__ and __cheaply__: within a few seconds and spending little energy
2. To let __anyone join__ the consensus process: no one has all the decision-making power
3. To let everyone __decide who to trust__: if you want to be trusted, you better play clean
4. To be __safe__: even if bad actors join the network, the network can still arrive at the "right" consensus

Before you say the first point is not important, consider 2 examples. A sequence of transactions that would cost 150 million dollars in fees over the traditional financial system only costs __20 cents__ over the Stellar network. The Bitcoin network has, as of January 2017, 2 [exahashes](https://en.wikipedia.org/wiki/Exa-) of processing power, which consumes as much energy as all of Ireland, and its network still takes ~30 minutes to process a transaction.

## A hard problem: consensus

__Reaching consensus__ is one of the hardest problems cryptocurrencies face.

The key issue with consensus is __trust__. It's hard to reach consensus with untrusted parties. What if Alice tells me to meet her at place X, but she goes to place Y? Of course, if Alice is my friend, I definitely trust her, but when it comes to the economy, with all sort of parties involved, it's unreasonable to trust everyone.

Now, the key issue with trust is __power__. It's easy to trust someone if we know there's some entity looming behind, more powerful than both of us, who can keep us honest.

__Currency__ is a form of __trust__ that is easy to quantify and divide, which what we want in order to do economic transactions. Without currency, transactions would be cumbersome. So, everyone wants to use currency because it's convenient. How can everyone agree on the _value_ of a given currency, though?

Say, If I were to mint some fiat currency, it would have __zero value__, because people would have __zero trust__ in it. Why? Because I have __zero power__. Sovereign states do have power, which is why people (usually) trust currencies minted by them. The less powerful a state, the less value any currenty minted by it would have, and, in the limiting case, a [failed state](https://en.wikipedia.org/wiki/Failed_state) may end up with a currency that has zero value.

<!-- but we both agree to trust this hypothetical "looming powerful entity" -->

<!-- This is what happens at the level of individuals and businesses. -->

<!-- And it's hard to trust someone who knows will go unpunished regardless of what she does. -->

<!-- The "trust problem" may be solved at the individual level, but the "solution" is kicking it to the next level in the hierarchy. Trust is an unsolved problem for sovereign states. Among parties with roughly equal power, without a "superior power" above, it's, by definition, impossible to __force__ anyone to do anything.

Which is why international relations can get complicated. The __United Nations__ (and the League of Nations before them) is a mechanism to somehow alleviate the problem of trust, but it's not a mathematical solution, and it could in theory fail at any given time (the League of Nations certainly did).
 -->

## What is a blockchain?

A __blockchain__ is a mathematical object whose main goal is to provide __trust__.

To do this, a __blockchain__ must reach consensus through some __consensus algorithm__.

So, currency is a form of trust, and blockchains are a mathematical way of providing trust. Can there exist currencies whose trust doesn't come from the power of a sovereign state, but from the power of mathematics?

The answer is yes.

## A solution: proof of work

The Bitcoin blockchain reaches consensus through a mechanism called [__proof of work__](https://en.wikipedia.org/wiki/Proof-of-work_system).

The first application of __proof of work__ was fighting spam. Each time Alice sent an email, the server required her computer to compute __hashes__; say, half a second worth of hashes. As a first approximation, we can see a __hash__ as the value of a function at some point. For example, the value of the __square function__ at the point 4 is 16, because 16 is the square of 4. A hash arises in the same way, but by using a function with special properties. That function is called a __hash function__.

To get an idea of what this looks like, the hash of `123` under a common hash function is `75263518707598184987916378021939673586055614731957507592904438851787542395619`.

So, __proof of work__ adds a small overhead to each email sent (half a second). This is small enough to go unnoticed by Alice, but a game-changer for spammers, who now must spend half a million seconds to send one million emails. How can the server verify that Alice has actually done all that work, though? The details are tricky:

The server arbitrarily chooses a number, say `1,000,000,000,000`. In Bitcoin this is called the __difficulty target__. The lower its value, the harder it is to compute. To arrive at this number, Alice must hash her email repeatedly, until she (by acccident) arrives at a number smaller than `1,000,000,000,000`, say `999,999,999,999`. Now, to verify Alice has actually ran tons and tons of hashes to arrive at `999,999,999,999` (or smaller), the server simply looks at Alice's hash and compares it to the one it has. If they're identical, the server _knows_ Alice did do all the work. This works because (good) hash functions are expected (but maybe not proved!) to behave randomly, it's possible to calculate how long she has to keep on computing until she finds the desired number by accident.

<!-- Say Bob wants to prove that he can do a really hard math question. Alice doesn’t know what the answer is, but she knows that the answer, when put through a SHA-256 hash, is 73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049. Bob completes the question and hashes his answer. Alice can then look at Bob’s hash and compares it to the hash she has, and if they are identical, then she knows Bob found the right answer. Alice still does not know the answer or how Bob got that result – but she knows that Bob arrived at the right answer. Bitcoin uses this type of a system for each block found – and each block relies on including the previously found block in the generated hash. This means as soon as a block is found and propagated through the network, all of the previous ‘work’ performed by miners is now irrelevant.
 -->

[Satoshi](https://en.wikipedia.org/wiki/Satoshi_Nakamoto) used __proof of work__ as a way to establish __consensus__. It's not at all obvious how one would do this, which is probably why it took so long for people to figure it out.


But the key to this relies in number-theoretic magic. Proof of work can only exist if there are functions that __hard__ in "one direction", but __easy__ in "another" one, in a precise technical sense.

An example of such objects are __hash functions__, which are easy to evaluate but near impossible to reverse. In our previous example, it's easy to arrive at `75263518707598184987916378021939673586055614731957507592904438851787542395619` if we're given `123`, but it's near to impossible to __calculate__ `123` if we only have `75263518707598184987916378021939673586055614731957507592904438851787542395619`.

<!-- ## Hash functions

There's only 1 formal requirement for a hash function: it must be __deterministic__. Useful hash functions must satisfy many other properties, 


Hash functions are designed to be near impossible to understand by analytic methods and simple formulas. They're designed so that the cheapest and easiest way is to __brute force__ the solution.


Actually, a cryptographic hash function can be used as an expensive pseudorandom number generator, and a pseudorandom number generator can be used as a weak, non-cryptographic hash function.
 -->

<!-- ## What is a blockchain


In a blockchain, a __transaction__ is a movement of currency between two parties. So, a blockchain is a data structure that keeps data on every piece of currency that moves throughout the network. A human would represent such a data structure in a long piece of paper, writing every single transaction by hand, like in the old accounting ledgers.

Blockchains, however, are special because they're __distributed__ ledgers of transactions.


To do this, __blockchains__ must reach consensus through some __consensus algorithm__. Consensus can be reached on a number of things, from the color people think the sun is, to the dining place for a groups of friends. Abstractly, consensus is an agreement on the value of a function given a a particular input.


Regardless of what the consensus is _about_, consensus needs one key thing: __trust__. 


In the future, I know it'll be hard to make plans with her


As mathematical objects, blockchains must have their properties __formally proved__. Afterwards, these properties are known to be _infallible_, forever, in the precise same way the derivative of sine is cosine, forever: their correctness becomes a __theorem__ of mathematics.

In general, we can't prove all things about a blockchain that we'd like to.


That is, in the Platonic world where they live, 


But perfect Platonic objects must be implemented in the physical, and in the implementation many things can go wrong.
 -->

<!-- ## What is a cryptocurrency

Money is a form of __trust__. 

[...]

The economy is build upon trust. Without trust, business is impossible. 


Trust is built on mathematics. How, specifically? By __computation__.
 -->

## Environmental friendliness

The mathematical foundations of blockchains come from [number theory](), and the computational complexity of certain objects, such as the [integers]() and [elliptic curves](). (Find out more about elliptic curves [here](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) and [here](https://medium.com/@VitalikButerin/exploring-elliptic-curve-pairings-c73c1864e627))These objects can get so complicated that certain problems on them are possible to solve but require more computational resources than what can be found in, say, the observable universe. This aspect is used as shelter against attackers.

On the other side, we can also reach consensus based on them, but it comes at a price: lots of (feasible) computation.

The two largest cryptocurrencies, by market capitalization (as of Jan 2017), are Bitcoin (USD 16 billion) and Ethereum (USD 1 billion). Both use different mechanics to reach consensus. They have different formal properties, making them, in particular, very expensive to compute. (Bitcoin, for instance, is starting to consume as much energy as [whole countries](http://motherboard.vice.com/read/bitcoin-could-consume-as-much-electricity-as-denmark-by-2020)). At these capitalizations, blockchains are still very small in the global economy, and scaling up some of these algorithms to the planetary level is a serious concern.

<!-- ## What is Stellar -->

Stellar is a decentralized financial platform that reaches consensus in a computationally cheap way. This grants the network a level of nimbleness that is mathematically difficult for other similar systems.

<!-- ## What is the Stellar Consensus Protocol

SCP is free of __blocked states__  

1. __Decentralized control__
2. __Low latency__
3. __Flexible trust__
4. __Asymptotic security__
 -->

<!-- ## Transaction fees -->

Every transaction has a .00001 XLM fee, as a deterrent to spammers, called the __base fee__. These funds are fed back to the Stellar network in the process of inflation. For more information [go here](https://www.stellar.org/developers/learn/concepts/inflation.html).

## A first dive into the Stellar network

But enough talk of ledgers, transactions, operations, and effects. What does the __state__ of the network actually _look like_? It's easy to take a peek using the REST API, which we'll access through Python.


    import requests  # Install by running `pip install requests` on the console
    from pprint import pprint


    class Horizon:
        """A thin Python wrapper around the Horizon REST API!"""

        def __init__(self, horizon_url='https://horizon.stellar.org'):
            self.horizon_url = horizon_url

        def metrics(self):
            return requests.get(self.horizon_url + '/metrics')

        def ledgers(self, limit=10, order='desc'):
            return requests.get(self.horizon_url + '/ledgers?limit=' + limit + '&order=' + order)

        def ledgers(self):
            return requests.get(self.horizon_url + '/ledgers?limit=10&order=desc')

        def account(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id)

        def trades(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/trades')

        def payments(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/payments')

        def transactions(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/transactions')

        def operations(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/operations')

        def effects(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/effects')

        def offers(self, account_id):
            return requests.get(self.horizon_url + '/accounts/' + account_id + '/offers')


    # This is an account on the real network that I created for testing purposes
    account_id = 'GAOXVBKHGKH3UNAK4EIG3XVAWMA4B7Y3LF42EMIKJINVMLTNXYGHUQWM'

    horizon = Horizon()

    response = horizon.metrics()
    pprint(response.json())

    response = horizon.ledgers()
    pprint(response.json())

    response = horizon.account(account_id=account_id)
    pprint(response.json())

    response = horizon.trades(account_id=account_id)
    pprint(response.json())

    response = horizon.payments(account_id=account_id)
    pprint(response.json())

    response = horizon.transactions(account_id=account_id)
    pprint(response.json())

    response = horizon.operations(account_id=account_id)
    pprint(response.json())

    response = horizon.effects(account_id=account_id)
    pprint(response.json())

    response = horizon.offers(account_id=account_id)
    pprint(response.json())


What does the output look like? It's a mess, isn't it? But at least it's human-readable, 

In time we'll turn this innocent-looking snippet into a powerful application that can do all sorts of useful things, from making simple payments to doing high-frequency trading. But before that, we'll go deeper into Stellar itself. The key idea is this: __federated Byzantine agreements__.

## Getting started

Here's 3 suggestions to start getting familiar with Stellar.

1. Read the official explanations: [example 1](https://medium.com/a-stellar-journey/on-worldwide-consensus-359e9eb3e949) [example 2](https://www.stellar.org/stories/adventures-in-galactic-consensus-chapter-1/) [example 3](https://www.stellar.org/blog/stellar-consensus-protocol-proof-code/)
2. Create an account in the [__testnet__](https://www.stellar.org/developers/guides/concepts/test-net.html), which you can fund freely with (fake) lumens.
3. Take a peek at the state of the Stellar ledgers, through the Horizon API
