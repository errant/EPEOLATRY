# Epeolatry
*(ˌɛpɪˈɒlətrɪ)*

*n.*

    Literally, the worship of words.

-------

Epeolatry is an opinionated, extensible library for the extraction and tidying up of words from various document sources; for example images or PDF's.

Given a file input, the library will attempt to isolate a relevant parser (using mime-type, primarily) and attempt to extract any textual content.

Epeolatry is intended to be extensible; please provide your own parsers either as pull requests or, where it makes sense, as external plugins (see "Adding Parsers"

# Install

Epeolatry is written for Python 3, and can be installed with Pip in the traditional way.

> pip3 install epeolatry


# Usage

The API is intentionally simple; Epeolatry is a library that is simplistic to interface with but provides complex internal functionality:

> import epeolatry
>
> doc = epeolatry.get_document_parser('/path/to/file.ext')
>
> doc.to_text()

# Parsers

The core of the library are Parsers which take a file input and spit out text. There are some built in parsers as part of the library. External parsers can be built and added at runtime using the setuptools entry_points functionality.

## Built-In Parsers

* PDF

## Adding Parsers

(coming soon)

# To Do

These are more next-level features rather than basic functionality:

* Document/Word classification
* De-Duplication
* Indexing

# Logging

Logging is implemented using the standard Python logging library.