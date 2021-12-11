(ns aoc-clj-2021.day7
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day7.txt") slurp (str/trim-newline)))
(def nums (map parse-long (str/split data #",")))
(defn diffs [v1 v2] (map #(Math/abs %) (map - v1 v2)))

;; part 1
(reduce + (apply min-key #(reduce + %)
                 (map #(diffs nums (repeat %)) nums)))
;; part 2
(defn range-sums [v1 v2]
  (map (fn [a b]
         (reduce + (range (inc (- (max a b) (min a b))))))
       v1 v2))

;; absurdly slow - also why is it that i had to use range nums here
;; vs just nums in the python solution?
(reduce + (apply min-key #(reduce + %)
                 (map #(range-sums nums (repeat %))
                      (range 0 (inc (apply max nums))))))
