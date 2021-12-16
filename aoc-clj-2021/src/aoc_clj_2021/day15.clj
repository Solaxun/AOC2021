(ns aoc-clj-2021.day15
  (:require [clojure.string :as str]
            [clojure.java.io :as io]))

(def data (str/split-lines (slurp (io/resource "day15.txt"))))

(def grid
  (->> (slurp (io/resource "day15.txt"))
       (str/split-lines)
       (mapv (fn [v] (mapv (comp parse-long str) v)))))

(defn neighbors [grid loc]
  (->> (mapv #(mapv + loc %) [[0 1] [1 0] [0 -1] [-1 0]])
       (filter #(get-in grid %))))

(defn find-cheapest [grid start neighbor-func end]
  (loop [q (sorted-set [0 start]) seen #{start}]
    (when-let [[cost [r c] :as node] (first q)]
      (if (= [r c] end)
        cost
        (recur (into (disj q node)
                     (map #(vector (+ cost (get-in grid %)) %)
                          (remove seen (neighbor-func [r c]))))
               (into seen (neighbor-func [r c])))))))

(defn add-mod [a b] (-> (+ a b) (dec) (mod 9) inc))

(defn expand-row [grid size]
  (->> grid
       (map (fn [row] (map-indexed (fn [i r] (map add-mod (repeat (* size (count r)) i) r))
                                   (repeat size row))))
       (mapv #(vec (apply concat %)))))

(defn expand-grid [grid size]
  (let [exp-rows (expand-row grid size)
        exp-cols (expand-row (apply map vector exp-rows) size)]
    (apply mapv vector exp-cols)))

(let [p1 (find-cheapest grid [0 0] #(neighbors grid %) [99 99])
      g2 (expand-grid grid 5)
      p2 (find-cheapest g2 [0 0] #(neighbors g2 %) [499 499])]
  (println p1)
  (println p2))
