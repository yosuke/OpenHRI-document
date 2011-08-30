#!/bin/sh

srgstojulius sample-en.grxml | juliustographviz | dot -Tpng > sample-grammar-en.png
srgstojulius sample-jp.grxml | juliustographviz | dot -Tpng > sample-grammar-ja.png
seatmltographviz sample-en.seatml | dot -Tpng > sample-script-en.png
seatmltographviz sample-jp.seatml | dot -Tpng > sample-script-ja.png

