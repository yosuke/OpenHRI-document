#!/bin/sh

srgstojulius flaggame-ja.grxml | juliustographviz | dot -Tpng > flaggame-ja-grammar.png

seatmltographviz flaggame-ja.seatml | dot -Tpng > flaggame-ja-script.png
