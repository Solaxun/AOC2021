(ns aoc-clj-2021.day10
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data (->> (io/resource "day10.txt") slurp str/trim-newline str/split-lines))
(def open->close {\( \) \[ \] \{ \} \< \>})
(def closed? (set (vals open->close)))

(defn bad-line? [line]
  (loop [opened []
         [l & ls] line]
    (if l
      (if (closed? l)
        (if (= (open->close (peek opened))
               l)
          (recur (pop opened) ls)
          l)
        (recur (conj opened l) ls))
      opened)))

(->> data
     (map bad-line?)
     (filter char?)
     (map {\) 3 \] 57 \} 1197 \> 25137})
     (reduce +))

(defn score-missing [missing]
  (let [score (apply hash-map (interleave "([{<" (range 1 5)))
        missing (reverse missing)]
    (reduce (fn [acc cur] (+ (* acc 5) cur))
            0
            (map score missing))))

(defn middle [xs]
  (nth xs (quot (count xs) 2)))

(->> data
     (map bad-line?)
     (filter vector?)
     (map score-missing)
     sort
     middle)
