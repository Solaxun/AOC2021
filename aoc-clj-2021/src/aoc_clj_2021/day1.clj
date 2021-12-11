(ns aoc-clj-2021.day1
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data
  (->> (io/resource "day1.txt")
       slurp
       str/split-lines
       (map parse-long)))

;; part 1
(->> (partition 2 1 data)
     (filter (fn [[x y]] (> y x)))
     count)

;; part 2
(reduce (fn [{:keys [count prev] :as state} [x y z]]
          (assoc (if (> (+ x y z) prev)
                   (update state :count inc)
                   state)
                 :prev (+ x y z)))
        {:count 0 :prev 0}
        (partition 3 1 data))

;; count minus 1, as we started with zero for prev instead of first
;; partition - so of course 1st partition sum is > 0.
