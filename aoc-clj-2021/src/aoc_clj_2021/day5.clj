(ns aoc-clj-2021.day5
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data
  (->> (io/resource "day5.txt")
       slurp))

(def points
  (->> (re-seq #"\d+" data)
       (map parse-long)
       (partition 4)))

(defn horizontal? [[x1 y1 x2 y2]]
  (= y1 y2))

(defn vertical? [[x1 y1 x2 y2]]
  (= x1 x2))

(defn diagonal? [[x1 y1 x2 y2]]
  (zero? (- (Math/abs (- x1 x2))
            (Math/abs (- y1 y2)))))

(defn connect-horizontal [[x1 y1 x2 y2]]
  (let [x2dir (if (> x2 x1) -1 1)]
    (map vector
         (cons x1 (take-while #(not= % x1)
                              (iterate #(+ % x2dir) x2)))
         (repeat y1))))

(defn connect-vertical [[x1 y1 x2 y2]]
  (let [y2dir (if (> y2 y1) -1 1)]
    (map vector
         (repeat x1)
         (cons y1 (take-while #(not= % y1)
                              (iterate #(+ % y2dir) y2))))))

(defn connect-diagonal [[x1 y1 x2 y2]]
  (let [x2dir (if (> x2 x1) -1 1)
        y2dir (if (> y2 y1) -1 1)]
    (cons [x1 y1](take-while #(not= % [x1 y1])
                             (iterate (fn [[x2 y2]] [(+ x2 x2dir) (+ y2 y2dir)])
                                      [x2 y2])))))

(defn connect-points [[x1 x2 y1 y2 :as points]]
  (cond
    (horizontal? points) (connect-horizontal points)
    (vertical? points) (connect-vertical points)
    (diagonal? points) (connect-diagonal points)
    :else (throw "problem!")))

(defn intersections [f]
  (->> points
       (filter f)
       (mapcat connect-points)
       (frequencies)
       (keep (fn [[item cnt]] (when (> cnt 1) 1)))
       (reduce +)))

(intersections #(or (vertical? %) (horizontal? %)))
(intersections #(or (vertical? %) (horizontal? %) (diagonal? %)))
