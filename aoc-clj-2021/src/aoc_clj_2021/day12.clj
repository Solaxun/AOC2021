(ns aoc-clj-2021.day12
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day12.txt") slurp str/trim-newline str/split-lines))

(def neighbors
  (->> (map #(str/split % #"-" ) data)
       (mapcat (fn [[from to]] [[from to] [to from]]))
       (reduce (fn [m [k v]] (update m k (fnil conj []) v)) {})))

(defn is-lower? [s] (= (str/lower-case s) s))
(defn neighbor-func [path]
  (->> (neighbors (last path))
       (remove #(and (contains? (set path) %) (is-lower? %)))))


(defn bfs-search [start next-moves is-goal?]
  (let [q (clojure.lang.PersistentQueue/EMPTY)]
    (loop [open (conj q [start])
           paths []]
      (cond (is-goal? (last (peek open)))
            (recur (pop open) (conj paths (peek open)))

            (empty? open) paths

            :else (recur (into (pop open)
                               (map #(conj (peek open) %)
                                    (next-moves (peek open))))
                         paths)))))


(count (bfs-search "start" neighbor-func #(= % "end")))

(defn neighbor-func-2 [path]
  (let [f (frequencies (filter is-lower? path))
        n (->> path last neighbors (remove #(= "start" %)))]
    (if (>= 1 (apply max (vals f)))
      n
      (remove #(and (>= (get f % 0) 1)
                    (is-lower? %))
              n))))

;; few times faster than python
(count (bfs-search "start" neighbor-func-2 #(= % "end")))
