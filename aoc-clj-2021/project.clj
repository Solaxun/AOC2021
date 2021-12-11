(defproject aoc-clj-2021 "0.1.0-SNAPSHOT"
  :description "advent of code 2021"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.11.0-alpha3"]
                 [org.clojure/math.combinatorics "0.1.6"]]
  :main ^:skip-aot aoc-clj-2021.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all
                       :jvm-opts ["-Dclojure.compiler.direct-linking=true"]}})
