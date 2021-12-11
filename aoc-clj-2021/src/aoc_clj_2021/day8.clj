(ns aoc-clj-2021.day8
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]
            [clojure.math.combinatorics :as combs]))

(def data (->> (io/resource "day8.txt") slurp str/trim-newline str/split-lines))

(def segment-digit-pairs
  (->> data
       (map #(str/split % #" \| "))
       (map (fn [v] (map #(str/split % #" ") v)))))

;; part 1
(->> segment-digit-pairs
     (mapcat second)
     (filter (fn [num] (contains? #{2 4 3 7} (count num))))
     (count))


;; part 2
(def ixs-to-nums
  {[0 1 2 3 4 5] 0
   [1 2] 1
   [0 1 3 4 6] 2
   [0 1 2 3 6] 3
   [1 2 5 6] 4
   [0 2 3 5 6] 5
   [0 2 3 4 5 6] 6
   [0 1 2] 7
   [0 1 2 3 4 5 6] 8
   [0 1 2 3 5 6] 9})

(defn find-letter-ix [item coll]
  (let [ix (.indexOf (seq coll) item)]
    (when (not= -1 ix) ix)))

(defn get-number [letters eight-config]
  (let [ixs (keep #(find-letter-ix % eight-config) letters)]
    (get ixs-to-nums (-> ixs sort vec))))

(defn gen-lookup [segments]
  ;; TODO: goes through every perm even if we already found a match -
  ;; consider reductions or some way to return early - about 10x slower than
  ;; python version, this is probably a big part of the reason
  (for [eight (combs/permutations "abcdefg")
        :let [segs (remove #(= 7 (count %)) segments)
              nums (keep #(get-number % eight) segs)]]
    (when (= 9 (count nums)) ; 9 bc we start with the tenth digit (eight)
      (assoc (zipmap (map sort segs) nums)
             (seq "abcdefg") 8)))) ; add back the 8

(defn seq->digit [xs]
  (parse-long (str/join xs)))

(->> (for [[lhs rhs] segment-digit-pairs
          :let [lkp (some identity (gen-lookup lhs))
                rhs (map sort rhs)]]
      (map lkp rhs))
     (map seq->digit)
     (reduce +))
