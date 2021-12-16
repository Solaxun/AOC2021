(ns aoc-clj-2021.day13
 (:require  [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (slurp (io/resource "day13.txt")))

(def coords
  (->> (re-seq #"(\d+),(\d+)" data)
       (map rest)
       (map #(map parse-long %))
       (set)))

(def folds
  (->> (re-seq #"([xy])=(\d+)" data)
       (map rest)
       (map (fn [[axis n]] [axis (parse-long n)]))))

(defn fold-coord [[x y] axis split-ix]
  (let [xadj (- x (* 2 (- x split-ix)))
        yadj (- y (* 2 (- y split-ix)))]
    (cond (and (= axis "x") (> x split-ix)) [xadj,y]
          (and (= axis "y") (> y split-ix)) [x,yadj]
          :else [x,y])))

(defn display-code [coords]
  (let [maxx (apply max (map first coords))
        maxy (apply max (map second coords))
        disp (vec (repeat (inc maxy) (vec (repeat (inc maxx) " "))))
        full (reduce #(assoc-in %1 (reverse %2) "#") disp coords)]
      (doseq [ln full] (println (str/join ln)))))

(let [[part1 part2-coords]
    (->> (reductions (fn [c [ax n]] (set (map #(fold-coord % ax n ) c)))
                    coords
                    folds)
        ((juxt (comp count second) last)))]
   (println part1)
   (display-code part2-coords))
