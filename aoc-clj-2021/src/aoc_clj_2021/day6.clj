(ns aoc-clj-2021.day6
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day6.txt") slurp (str/trim-newline)))
(def nums (map parse-long (str/split data #",")))

;; part 1
(-> (iterate (fn [nums] (mapcat #(if (zero? %) [6 8] [(dec %)]) nums))
             nums)
    (nth 80)
    count)

;; part 2
(def fish (merge (apply hash-map (interleave (range 9) (repeat 0)))
                 (frequencies nums)))

(defn evolve-fish [fish]
  (let [newfish (fish 0 0)]
    (->> fish
         (mapcat (fn [[i cnt]]
                   (cond (zero? i) [8 newfish]
                         (= 6 i) [6 (+ newfish (fish 7 0)) 5 (fish 6 0)]
                         :else [(dec i) (fish i 0)])))
         (apply hash-map))))


(reduce + (-> (iterate evolve-fish fish) (nth 256) (vals)))
