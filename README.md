Internet Archive
================

An updated website concept for archive.org

## Concept

To increase interaction and participation on archive.org by providing a UI which is more conducive of a search engine experience. The new design emphasized + highlights forms of media which are most likely (statistically) to be requested or accessed by users.

## Installation

    git clone http://github.com/mekarpeles/archive.org
    cd archive.org
    sudo pip install -e .

## Dependencies

(see setup.py) waltz, requests, markdown. Dependencies resolved via 'pip install -e'.

## Todo

[ ] integrate wayback into search results
- e.g. http://web.archive.org/web/20120401000000*/http://google.com
[ ] fix vertical faceted search (categories)
- right now they are all routed through advancedsearch.php (no mediatype, defaulting to all)
[ ] async ajax json serp (w/ files links)
- after initial serp is returned, ajax load add'l data for each result
[ ] Drop down menus for categories in top menu
- like audio -> music