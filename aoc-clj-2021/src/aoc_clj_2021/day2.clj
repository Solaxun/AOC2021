(ns aoc-clj-2021.day2
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data
  (->> (io/resource "day2.txt")
       slurp
       str/split-lines
       (map #(str/split % #" "))
       (map (fn [[dir amt]] [dir (parse-long amt)]))))

(let [{:strs [forward up down]}
      (->> (group-by first data)
           (map (fn [[dir amts]] [dir (reduce + (map second amts))]))
           (into {}))]
  (* forward (- down up)))

;; part 2

(let [{:keys [aim horizontal depth]}
      (reduce (fn [{:keys [aim horizontal depth] :as state} [dir amt]]
                (case dir
                  "forward" (-> (update state :horizontal + amt)
                                (update :depth + (* aim amt)))
                  "up"      (update state :aim - amt)
                  "down"    (update state :aim + amt)))
              {:aim 0 :horizontal 0 :depth 0}
              data)]
  (* depth horizontal))
