(ns aoc-clj-2021.day4
  (:require [clojure.string :as str]
            [clojure.set :as set]
            [clojure.java.io :as io]))

(def data
  (->> (io/resource "day4.txt")
       slurp
       str/split-lines
       (remove #(= "" %))))

(def hand (->> (-> data first (str/split #","))
               (map parse-long)))

(def boards
  (->> (for [row (rest data)
             :let [parsed (->> (str/split row #" ")
                               (remove #(= "" %))
                               (map parse-long))]]
         (vec parsed))
       (partition 5)
       (map vec)))

(defn place-piece [piece board]
  (vec (for [[r row] (map-indexed vector board)]
        (vec (for [[c col] (map-indexed vector row)]
               (if (= col piece)
                 "*"
                 col))))))

(defn row-full? [row]
  (every? #(= % "*" ) row))

(defn winner? [board]
  (or (some row-full? board)
      (some row-full? (apply map vector board))))

(defn play-round [piece boards]
  (let [bs (map #(place-piece piece %) boards)
        winner (filter winner? bs)]
    (when (seq winner) winner)))

(defn score [num-called board]
  (* num-called
     (->> board
          flatten
          (remove #(= % "*"))
          (reduce +))))

;; part 1
(reduce (fn [boards piece]
          (let [bs (map #(place-piece piece %) boards)
                w  (filter winner? bs)]
            (if (seq w)
              (reduced (score piece (first w)))
              bs)))
        boards
        hand)

;; part 2
(-> (reduce (fn [{:keys [boards winners] :as state} piece]
              (let [bs (map #(place-piece piece %) boards)
                    w  (filter winner? bs)]
                (if (seq w)
                  (-> (update state :winners conj (score piece w))
                      (assoc :boards (remove winner? bs)))
                  (assoc state :boards (remove winner? bs)))))
            {:boards boards :winners []}
            hand)
    :winners
    last)
