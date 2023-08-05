# README

This README is for word segmentation module based on Hierarchical 
Dirichlet Processes (Goldwater PhD thesis, 2007; Mochihashi et
al., ACL 2009), or *HDP Wordseg* in short.

This implementation is developed by Prachya Boonkwan, Language and
Semantic Technology Lab, National Electronics and Computer
Technology Center (NECTEC), Thailand.

(C) April 2015. All right reserved.


## Requirements

The script is written in Python 2.7 programming language. It
is self-contained and requires no additional libraries.
However, PyPy is used for speed enhancement and the script
automatically calls PyPy by default.


## How to Run

The HDP Wordseg can be run by calling the script `hdpwordseg`.
In Unix, key in the following instruction (`$` is the Unix
prompt).

    $ hdpwordseg

Calling the script without any arguments will display its usage.
If you want more explanation, simply call

    $ hdpwordseg -h

A more elaborate help message will appear.


### Basic Setting

To run the most basic setting of unsupervised word segmentation,
add the following arguments: `-n`, `-c`, and `-l`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 text1.txt text2.txt ...

This setting has the following specification:

1. Word-level model: trigram (`-n 3`)
2. Character-level model: 5-gram (`-c 5`)
3. Maximum word length: 10 (`-l 10`)
4. Number of iterations: 100 loops (`-i 100`)
5. Input files: `text1.txt`, `text2.txt`, ...

The script will read the input files to the memory, taking
each character as an atomic unit. The HDP model is then
estimated with Gibbs sampling, in which words are formed
by biased randomization (governed by the probability
distribution) from consecutive atomic units. Once finished,
the Viterbi algorithm is run to select the most probable
way of word segmentation w.r.t. the estimated model. The
output will be shown on the standard output channel (i.e.
the display).

Please note that some optimization has also been applied to
the sampling process, including forward filtering and
backward sampling, hyperparameter resampling, and Poisson
regulation. These optimization techniques can be turned off
as will be explained later.


### $n$-gram Models

The HDP model used in this implementation consists of two
levels of $n$-gram models: the character-level model and
the word-level model.

- The character-level model can be of one or more grams.
- The word-level model can be, however, either unigram 
  or bigram.


### Redirecting to Output File

This implementation can also generate an output text file
instead of displaying it on the screen. To do so, add the
argument `-o`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -o output.txt text1.txt text2.txt ...

The additional argument specifies that the system will
produce the output file `output.txt` (`-o output.txt`) as
a result of word segmentation.


### Delimiters

This implementation accepts both raw text and processed text.
That is, the text has already been annotated with unit
boundary markers, called *delimiters*.

In the case where there are delimiters present in the input
files, you can also specify them by using the argument
`--delim`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --delim '|' text1.txt text2.txt ...

The additional argument specifies that the delimiters are `|`,
meaning that each line in the input files is in the following
form:

    atom1|atom2|atom3|...

If the tailing delimiters are present (e.g. `a1|a2|a3|`), they
will be neglected (i.e. equal to `a1|a2|a3`).


### White Spaces

If the input text contains white spaces that can be used as
word or sentence delimiters, it can also be used to reduce
the size of the search space for word segmentation and
speed up the training process. The white space can be
identified by using the argument `--space`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --delim '|' --space '_' text1.txt text2.txt ...

The additional argument specifies that the white spaces are
`_`, meaning that each line in the input files is in the
following form:

    atom|atom|atom|...|_|atom|atom|atom|...

where `_` is the white space separating two consecutive
chunks of text.


### Disk-Based Cache

In the case where memory is concerned, the option `--cache`
can be used to enable the disk-based cache. For example,

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --cache text1.txt text2.txt ...

The additional argument means that now the unigram and
bigram probability tables are now cached in the disk. This
cache will be automatically emptied after the word
segmentation is done.

Please note that the cache mode will be automatically activated
if the input contains more than 10,000 tokens in total.


### Configuration File

For ease of experiment setting, this software accepts the
notion of configuration files. A configuration file can be
specified by the argument `--config`.

    $ hdpwordseg --config myconfig.cfg text1.txt text2.txt ...

In the above example, the configuration file `myconfig.cfg`
is used for the setting.

**WARNING:** If the configuration file is present, the options
specified in it will take over the arguments by the command
line.

The format of the configuration files will be explained in
the chapter CONFIGURATION.


### *WARNING*

In practice, it is NOT recommended to run the script on each
input file separately if unnecessary. The HDP model is
estimated based on input files given at a time. Running on
them separatedly may result in separate models and different
word segmentation strategies.


## More Advanced Settings

If you want to adopt more advanced settings, there are three
combinable options: Metropolis-Hastings sampling, simulated
annealing, and partial supervision with dictionaries.


### Metropolis-Hastings Sampling

This implementation features Metropolis-Hastings sampling
as the alternative of Gibbs sampling. The advantage of using
Metropolis-Hastings sampling is that it is more independent
from the initial point of sampling than Gibbs sampling,
resulting in more reliable samples.

Metropolis-Hastings sampling can be run by specifying the
number of burn-in iterations, where samples generated
randomly are used to update the parameters for a certain
time. After the burn-in process, the sampling will
meticulously select the next sample from the current point
by considering its possibility of reaching an optimum.

To activate Metropolis-Hastings sampling, simply add the
argument `-b`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -b 30 text1.txt text2.txt ...

The additional argument specifies that we now require 30
burn-in iterations (`-b 30`) before the meticulous sampling.
The total number of iterations is still 100.


### Simulated Annealing

Simulated annealing helps the model converge faster. It
smooths, or 'statistically melts', the predictive
probability of each sample choice by computing its power
of $10^{-t}$ ; that is, the annealed probability $\hat{p}$
can be computed by:

$$ \hat{p} = p^{10^{-t}} $$

where $p$ is the real predictive probability, and $t > 0$
is the current temperature. The temperature then gradually
cools down to 0, revealing the true probability and thus
the name 'annealing'.

Simulated annealing can be activated by adding the
argument `-t`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -t 5 text1.txt text2.txt ...

The additional argument specifies that the maximum
temperature is set to 5 (`-t 5`).


### Topic Models

Topic models are shown to improve the accuracy of various
ML tasks. An additional latent variable, called *topic*,
is incorporated to the model to distinguish the
probability distributions among groups of observed data.

To activate the topic model, simply add the argument
`--topics`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --topics 3 text1.txt text2.txt ...

The additional argument specifies that there are at most
3 topics (`--topics 3`) in the model.

Furthermore, the topic models can also be extended to
Latent Dirichlet Allocation by adding the argument `--lda`

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --topics 3 --lda text1.txt text2.txt ...


### Partial Supervision with Dictionaries

Partial supervision can be introduced to unsupervised
word segmentation, where patterns of words and syllables
can be used as a guide to better segmentation. In this
implementation, we call such collection of patterns a
dictionary. This implementation accepts two kinds of 
dictionaries: atomic dictionary and word dictionary.

1. Atomic dictionary: a collection of unambiguous
   non-overlapping unit patterns, such as syllables and
   character clusters
2. Word dictionary: a collection of words or
   patterns of words which can be overlapping

We can incorporate both dictionaries in word segmentation
by adding the following arguments: `-a` and `-d`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -a atomdict.txt -d worddict.txt text1.txt text2.txt ...

The additional arguments specify that we want to use file
`atomdict.txt` as the atomic dictionary (`-a atomdict.txt`)
and file `worddict.txt` as the word dictionary (`-d
worddict.txt`).

Note that the patterns specified in these dictionaries
are not affected by the maximum length of words (e.g.
`-l 10`). This is because all atoms and words specified in
the dictionaries are recognized before guessing the word
boundaries.


#### Format

The format of these dictionaries are similar. They are
a simple text file, each line for a word or pattern,
for example, a line in these files may be a regular
expression such as the following:

    [0-9]+

which recognizes consecutive digits. It is required to
write each word or pattern in regular expression. In
the case where words contain symbols in regular
expression, do escape these symbols with the backslash
`\`. For example,

    [a-z0-9\_\.]\@[a-z0-9\-\.]+

that recognizes simple email addresses.


#### Macros

For ease of management, this implementation offers the
capability of defining macros for regular expressions.
This can be done by using the command `@define` in a
dictionary file. For example,

    @define <leading> 0|(\+[0-9]{1,3})
    @define <body> [0-9]+

The above commands define two macros `<leading>` and
`<body>` representing the above regular expressions,
respectively. Bracketing the macro's name with `< >`
is optional but recommended.

Once a macro is defined, it can be used throughout the
remainder of the dictionary file, e.g.

    <leading>(\-<body>)+

These macros will be expanded into their regular
expressions when loaded into the memory.

Each macro can also be defined more than one time, meaning
a disjunction of patterns, e.g. if `<consonant>` is
defined as follows.

    @define <consonant> b
    @define <consonant> c
    @define <consonant> d
    @define <consonant> f
    @define <consonant> g

This is equivalent to defining `<consonant>` as:

    @define <consonant> b|c|d|f|g


#### Comments

This implementation allows comments in the dictionary files.
Commenting can be done by adding `#` at the beginning of
each line. For example,

    # Pattern of telephone numbers
    @define <leading> 0|(\+[0-9]{1,3})
    @define <body> [0-9]+
    <leading>(\-<body>)+

Please note that inline comments are still not allowed.


## Hyperparameter Settings

There are three hyperparameters of the HDP model:
$\alpha$ , $\theta$ , and $p_{stop}$ .

- $\alpha$ : The discount parameter, specifying how
  less likely it is to choose a seen instance instead
  of an unseen one. It smoothes the count of the seen
  instance by deducting the count with its value.
  [ $0 \leq \alpha < 1$ ]
- $\theta$ : The strength parameter, specifying how
  likely it is to choose an unseen instance instead of
  the already seen ones. It smoothes the count of the
  unseen instance by adding the count with its value.
  [ $\theta \geq 0$ ]
- $p_{stop}$ : The probability of stopping generating
  the next character after the previous ones in a word.
  [ $0 < p_{stop} < 1$ ]

These hyperparameters can be set by the arguments: `--alpha`,
`--theta`, and `--pstop`, respectively.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 --alpha 0.1 --theta 1.0 --pstop 0.5 text1.txt text2.txt ...

Their default values are listed below.

- $\alpha$ = 0.0
- $\theta$ = 1.0
- $p_{stop}$ = `None` (unused)


## Disabling Advanced Optimization

Normally you do not have to turn off default optimization
except for experiment purposes. In this implementation,
some default optimizations can be turned off. They include
forward filtering and backward sampling, hyperparameter
resampling, Poisson regulation, and Viterbi decoding.


### Forward Filtering and Backward Sampling

Forward filtering and backward sampling is enabled by
default. Sampling proceeds based on expectation rather
than Gibbs's predictive probability. Although forward
filtering and backward sampling yields better results,
it can be disabled for baseline experiments. To do so,
simply add the argument `-F`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -F text1.txt text2.txt ...


### Hyperparameter Resampling

The hyperparameters of the HDP models are resampled in
each iteration of Gibbs sampling by default. However,
they can be fixed throughout the iterations by adding
the argument `-S`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -S text1.txt text2.txt ...


### Poisson Regulation

The base distribution for words is regulated by a Possion
distribution whose mean is the average length of word
lengths by default. This regulation improves the accuracy
of word segmentation as shown in Mochihashi et al. (2009).
The Poisson regulation can be disabled by adding the
argument `-R`.

    $ hdpwordseg -n 3 -c 5 -l 10 -i 100 -R text1.txt text2.txt ...


## Configuration

An additional configuration file can also be used in this
implementation by specifying the argument `--config`. For
example,

    $ hdpwordseg --config myconfig.cfg text1.txt text2.txt ...

In the above example, the configuration file `myconfig.cfg`
is used for the setting.

The format of the configuration file follows RFC 822 (Section
3.1.1 "Long Header Fields"), resembling Windows's INI format.
An example of a configuration file is shown below.

    [Output]
    output=output.txt
    
    [Model]
    word-gram=3
    char-gram=5
    topics=2
    LDA=on
    
    [Content]
    max-word-len=20
    delim='|'
    space=' '
    word-dict=dict.txt
    atom-dict=atom.txt
    
    [Hyperparameters]
    alpha=0.1
    theta=1.0
    pstop=0.2
    
    [Experiment]
    iters=100
    burnin=30
    max-temp=5
    fwdbwd=on
    hparamsmp=off
    poisson=off
    beamsize=10
    verbose=on
    debug=off
    cache=off

The configuration file contains five sections as follows.

1. Output: the output file
2. Model: the model's specification
3. Content: specifying the content of the input text files
4. Hyperparameters: the model's hyperparameters
5. Experiment: the experiment setting


### Output

The output section has only one option: `output`. It
specifies the output file for word segmentation, equivalent
to specifying the option `-o`. 

    [Output]
    output=myoutput.txt

If this line is missing or commented out (by preceding the
line with `#`), the output will be redirected to the
standard output (i.e. the screen).


### Model

This section specifies the model used in this experiment. It
contains four options: `word-gram`, `char-gram`, `topics`,
and `LDA`. For example,
    
    [Model]
    word-gram=3
    char-gram=5
    topics=2
    LDA=on

By these lines, the model used in this setting is word-level
trigrams (`word-gram=3`), character-level five-grams
(`char-gram=5`), having two latent topics (`topics=2`), and 
using Latent Dirichlet Allocation in assigning the topics
(`LDA=on`).

The option `topics` is optional. If it is missing or commented
out, the software assumes no latent topics in the dataset.
Otherwise, the topic model will be used in the experiment.

There are two topic models: the default HDP one (Mochihashi et
al., ACL 2009) and the LDA mixture (Blei et al., JMLR 2003).
The first one can be activated by specifying the option
`LDA=off` or commenting this option out. The latter option can
be activated by specifying `LDA=on` (equivalent to the argument
`--lda`).


### Content

This section specifies the characteristics of the content of
the input files. There are five options in this section:
`max-word-len`, `delim`, `space`, `word-dict`, and `atom-dict`.
    
    [Content]
    max-word-len=20
    delim='|'
    space=' '
    word-dict=dict.txt
    atom-dict=atom.txt
    
With these lines, the content has the following specification.

- The maximum word length is 20 (`max-word-len=20`), equivalent to
  the argument `-l 20`.
- The delimiter is `|` (`delim='|'`), equivalent to the argument
  `--delim '|'`.
- The white space is ` ` (`space=' '`), equivalent to the argument
  `--space ' '`.
- The word dictionary is `dict.txt` (`word-dict=dict.txt`),
  equivalent to the argument `-d dict.txt`.
- The atomic dictionary is `atom.txt` (`atom-dict=atom.txt`),
  equivalent to the argument `-a atom.txt`.

Each of these lines is optional. It can be commented out or
missing from the configuration and its default value will be
used (cf. the command line arguments for their defaults).


### Hyperparameters

Hyperparameters can also be specified in the configuration file.
In this section, there are three adjustable hyperparameters: 
`alpha`, `theta`, and `pstop`. For example,

    [Hyperparameters]
    alpha=0.1
    theta=1.0
    pstop=0.2

Please note that these lines are optional. They can be commented
out or missing from the configuration file and its default values
will be used instead (cf. the command line arguments for their
defaults).


### Experiment

This section is dedicated for experiment setting. There are 10
options available: `iters`, `burnin`, `max-temp`, `fwdbwd`,
`hparamsmp`, `poisson`, `beamsize`, `verbose`, `debug`, and
`cache`. For example,
    
    [Experiment]
    iters=100
    burnin=30
    max-temp=5
    fwdbwd=on
    hparamsmp=off
    poisson=off
    beamsize=10
    verbose=on
    debug=off
    cache=off

Each line results in the following specification:

- Maximum number of iterations: 100
- Burn-in iterations: 30
- Maximum temperature for simulated annealing: 5
- Forward filtering/backward sampling: *on*
- Hyperparameter resampling: *off*
- Poisson regulator: *off*
- Beam size: 10
- Verbose mode: *on*
- Debug mode: *off*
- Cache mode: *off*

These options correspond to their command line arguments. They
are also optional -- they can be commented out or missing from
the configuration file and their default values will be used.
