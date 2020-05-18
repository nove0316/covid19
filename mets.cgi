#!/usr/bin/ruby
# -*- coding: utf-8 -*-

require("cgi")
require("csv")


#htmlからの入力
input = CGI.new
#運動METs表のCSV[[コード, METs, カテゴリ, 活動], ]
data = CSV.read("")

#入力された運動のMETsの合計値
mets_sum = 0;

