(ns aoc-clj-2021.day11
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day11.txt") slurp str/trim-newline str/split-lines))
(def octopi (->> data (mapv vec) (mapv (fn [v] (mapv (comp parse-long str ) v)))))

(defn inc-by-one [[octopi flashed?]]
  [(mapv #(mapv inc %) octopi)
   flashed?])

(defn neighbors [loc]
  (for [i [-1 0 1] j [-1 0 1] :when (not= [i j] [0 0])]
    (mapv + loc [i j])))

(defn flash-step [[octopi flashed?]]
  (let [will-flash (set (for [[r row] (map-indexed vector octopi)
                              [c col] (map-indexed vector row)
                              :when (and (> col 9) (not (flashed? [r c])))]
                          [r c]))
        neighbors (->> will-flash (mapcat neighbors)  (remove #(nil? (get-in octopi %))))
        oct (reduce #(update-in %1 %2 inc) octopi neighbors)]
    [oct (set/union will-flash flashed?)]))

(defn wont-flash [octopi]
  (->> (keep-indexed (fn [r row]
                       (keep-indexed (fn [c col] (when (<= col 9) [r c]))
                                     row))
                     octopi)
       (apply concat)
       (set)))

(defn flash-step-done? [[octopi flashed?]]
  (= 100 (count (set/union (wont-flash octopi) flashed?))))

(defn reset-flashed [[octopi flashed? total-flashed]]
  [(reduce #(assoc-in %1 %2 0) octopi flashed?)
   #{}
   (+ total-flashed (count flashed?))])

(defn full-step [[octopi flashed? total-flashed :as state]]
  (let [step (->> [octopi flashed?]
                  (inc-by-one)
                  (iterate flash-step)
                  (some #(when (flash-step-done? %) %)))]
    (reset-flashed (conj step total-flashed))))

;; part 1
(let [[_ _ total-flashes] (nth (iterate full-step [octopi #{} 0]) 100)]
  total-flashes)

;; part 2
(some (fn [[i [octopi _ _]]]
        (when (->> octopi flatten (every? zero?)) i))
      (map vector
           (iterate inc 0)
           (iterate full-step [octopi #{} 0])))
