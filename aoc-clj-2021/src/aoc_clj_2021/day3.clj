(ns aoc-clj-2021.day3
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data
  (->> (io/resource "day3.txt")
       slurp
       str/split-lines))

(defn calc-rate [rate-type]
  (let [lkp {:gamma second :epsilon first}]
    (->> (apply map vector data)
         (map frequencies)
         (map (partial sort-by second)) ; sort maps by value (freq)
         (map (lkp rate-type)) ; smallest freq is first, largest second
         (map first)           ; get num from [num freq] pairs
         (str/join)
         (#(Integer/parseInt %  2)))))

(* (calc-rate :gamma)
   (calc-rate :epsilon))

;; part 2

(defn get-common [f xs]
  (let [nums (group-by identity xs)
        most-or-least (f (sort-by (comp count val) nums))
        tie-breaker (if (= f first) \0 \1)]
    (if (apply = (map count (map val nums)))
      tie-breaker
      (first most-or-least))))

(def get-most-common  (partial get-common last))
(def get-least-common (partial get-common first))

(defn rating [f]
  (loop [i 0 d data]
    (if (> (count d) 1)
      (let [common (map f (apply map vector d))]
        (recur (inc i)
               (filter #(= (nth % i) (nth common i))
                       d)))
      (Integer/parseInt (first d) 2))))

(def o2-gen (rating get-most-common))
(def co2-scrub (rating get-least-common))

(* o2-gen co2-scrub)
