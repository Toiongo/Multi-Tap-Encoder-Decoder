# Multi-Tap-Encoder-Decoder
Keyboard phones multi-tap encoding/decoding.

Old phones used to have layout where you'd need to press a button multiple times to get your letter or symbol.
It looked something like this:
------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |     | |     |
|  *  | |  0  | |  #  |
------- ------- -------

This can be used as a cypher of sorts, so i've made a program that allows you to encode strings in such a manner.
An example, the result for encoding "Hello" would be: 4433555555666.
Hopefully, you get the gist of it.
