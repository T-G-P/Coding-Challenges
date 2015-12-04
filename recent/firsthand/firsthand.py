"""
Author: Tobias Perelstein
=========================

README
======

Python was chosen due to its available data structures, peformance
and more specifically the Set data structure as it does not
allow insertion of duplicates. With php, I'd have used array_unique.
I will happily provide  similar solution with php.

To make things more extensible and universal, I could have this program
take in command line arguments for the text file, but for the purpose
of this excercise, I hard coded the input and output.


Algorithms and Data Structures
==============================

The words.txt file is opened and iterated through using
a the optional length parameter that defaults to 4. Each
line is iterated through until the last sequence of 'length'
(in this case 4) characters are a available. The sequence map
is then set at this sequence as the key with its value being
an empty set. A set was chosen so that the same sequence does not
hash to the same word twice in the event the word appears in the
words.txt file multiple times.

After the map is built, the output files are opened and the map
is iterated through in alphabetical order by key. If the key hashes
to a single word only, the word is added to fullwords.txt and the key
is added to uniques.txt

Overall complexity O(n^2)


Performance
===========
Using a single core machine, here is the output of the time command:

time firsthand.py

real    0m0.499s
user    0m0.419s
sys     0m0.019s

Using the time and timit python modules:

In [2]: %time main()
CPU times: user 151 ms, sys: 15.5 ms, total: 167 ms
Wall time: 185 ms

In [3]: %timeit main()
10 loops, best of 3: 128 ms per loop


I implemented the solution on a single core machine with the following specs:

In [5]: cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 62
model name      : Intel(R) Xeon(R) CPU E5-2630L v2 @ 2.40GHz
stepping        : 4
microcode       : 0x1
cpu MHz         : 2399.998
cache size      : 15360 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse
sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl eagerfpu pni pclmulqdq vmx ssse3 c
x16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm xsaveopt v
nmi ept fsgsbase tsc_adjust smep erms
bogomips        : 4799.99
clflush size    : 64
cache_alignment : 64
address sizes   : 40 bits physical, 48 bits virtual
power management:


"""

SEQUENCE_MAP = {}


def process_file(length=4):
    with open('words.txt') as f:
        for line in f:
            for i in range(len(line)-length):
                sequence = line[i:length+i]+'\n'
                if not SEQUENCE_MAP.get(sequence):
                    SEQUENCE_MAP[sequence] = set()
                SEQUENCE_MAP[sequence].add(line)


def build_results():
    with open('uniques.txt', 'w') as f1:
        with open('fullwords.txt', 'w') as f2:
            for key, val in sorted(SEQUENCE_MAP.items()):
                if len(val) == 1:
                    f1.write(key)
                    for word in val:
                        f2.write(word)


def main():
    process_file()
    build_results()


if __name__ == '__main__':
    main()
