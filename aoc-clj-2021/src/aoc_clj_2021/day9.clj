(ns aoc-clj-2021.day9
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day9.txt") slurp str/trim-newline str/split-lines))

(def grid
  (->> (map vec data)
       (mapv (fn [coll] (mapv #(-> % str parse-long) coll)))))

(defn neighbors-4 [loc]
  (map (fn [pt1 pt2] (map + pt1 pt2))
       [[0 1] [1 0] [0 -1] [-1 0]]
       (repeat loc)))

(def index->lowpoint
  (->> (for [[r row] (map-indexed vector grid)
             [c col] (map-indexed vector row)
             :let [neighbors (->> (neighbors-4 [r c]) (map #(get-in grid %)) (remove nil?))]
             :when (< col (apply min neighbors)) ]
         [[r c] col])
       (into {})))

;; part 1
(reduce + (map inc (vals index->lowpoint)))

;; part 2 - wanted to do without loop/recur and managing a stack/queue but honestly
;; would have been cleaner.
(defn find-basins [[loc num]]
  (let [visited? (atom #{})]
    (letfn [(expand [[loc num]]
              (let [uphill-neighbors
                    (->> (neighbors-4 loc)
                         (remove @visited?)
                         (keep #(when-let [x (get-in grid %)]
                                  (when (and (> x num) (not= 9 x))
                                    [% x]))))]
                (swap! visited? into (conj (mapv first uphill-neighbors) loc))
                (concat
                 (map vector (map first uphill-neighbors) (repeat num))
                 (mapcat expand
                         (map vector (map first uphill-neighbors) (repeat num))))))]
      (conj (expand [loc num])
            [loc num]))))

(->> (map find-basins index->lowpoint)
     (map count)
     (sort)
     (take-last 3)
     (reduce *))
