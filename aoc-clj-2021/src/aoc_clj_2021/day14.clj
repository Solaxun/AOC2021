(ns aoc-clj-2021.day14
  (:require [clojure.string :as str]
            [clojure.java.io :as io]))

(def data (str/split-lines (slurp (io/resource "day14.txt"))))
(def poly  (first data))
(def start (frequencies (partition 2 1 poly)))
(def rules
  (->> (drop 2 data)
       (map #(str/split % #" -> " ))
       (map (fn [[[a b] [to]]] [[a b] [[a to] [to b]]]))
       (into {})))

(defn multimap-combine [mm]
  (reduce (fn [m [c n]] (update m c (fnil + 0) n)) {} mm))

(defn step-poly [poly-freq]
  (->> (mapcat (fn [[pair cnt]] (interleave (get rules pair) (repeat cnt)))
               poly-freq)
       (partition 2)
       (multimap-combine)))

(let [final-poly {(last poly) 1}]
  (->> (nth (iterate step-poly start) 40) ;; change 40->10 for part 1
       (map (fn [[[p1 p2] n]] [p1 n]))
       (multimap-combine)
       (merge-with + final-poly)  ;; add back final polymer half
       (vals)
       (apply (juxt max min))
       (apply -)))
