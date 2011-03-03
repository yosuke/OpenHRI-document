#!/bin/sh

srgstojulius sample-en.grxml | juliustographviz | dot -Tpng > sample-grammar-en.png
srgstojulius sample-jp.grxml | juliustographviz | dot -Tpng > sample-grammar-ja.png

