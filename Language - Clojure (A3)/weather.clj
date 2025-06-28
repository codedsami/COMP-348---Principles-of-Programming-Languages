(ns weather
  (:require [clojure.string :as str]))            

(declare main-menu handle-choice)

(defn parse-line
  "Parses a comma-separated line into a weather report map."
  [line]
  (let [[date location temp condition] (str/split line #",")]
    {:date date
     :location location
     :temperature (Integer/parseInt temp)
     :condition condition}))

(defn load-reports
  "Loads weather reports from a file.
  Please refer to https://clojure.org/guides/threading_macros for more details on ->>
  "
  [filename]
  (if (.exists (java.io.File. filename))
    (->> (slurp filename)
         str/split-lines
         (map parse-line)
         vec)
    []))

(defn save-reports
  "Saves reports to a file (optional)."
  [reports]
  (spit "weather_output.txt"
        (clojure.string/join
         "\n"
         (map (fn [{:keys [date location temperature condition]}]
                (str date "," location "," temperature "," condition))
              reports)))
  (println "Reports saved to weather_output.txt"))


(defn view-weather-reports
  "Displays weather reports in a formatted table, sorted by date and with units."
  [reports]
  (let [sorted (sort-by :date reports)]
    (println (str "Total Reports: " (count sorted)))
    (println (format "%-12s | %-15s | %-15s | %-10s" "Date" "Location" "Temperature" "Condition"))
    (println (apply str (repeat 66 "-")))
    (doseq [{:keys [date location temperature condition unit]} sorted]
      (let [unit-str (or unit "C")]
        (println (format "%-12s | %-15s | %-15s | %-10s"
                         date location (str temperature "°" unit-str) condition))))))





(defn filter-weather-reports
  "Filters reports by condition or temperature range."
  [reports]
  (println "Filter by:\n1. Condition\n2. Temperature Range")
  (print "Enter your choice: ") (flush)
  (let [choice (read-line)]
    (cond
      (= choice "1")
      (do
        (print "Enter condition (case-sensitive): ") (flush)
        (let [cond (read-line)
              filtered (filter #(= cond (:condition %)) reports)]
          (if (empty? filtered)
            (println "No matching reports found. (Tip: Make sure you're using the correct condition.)")
            (view-weather-reports filtered))))

      (= choice "2")
      (do
        (print "Min temperature: ") (flush)
        (let [min-temp (Integer/parseInt (read-line))]
          (print "Max temperature: ") (flush)
          (let [max-temp (Integer/parseInt (read-line))
                filtered (filter #(and (>= (:temperature %) min-temp)
                                       (<= (:temperature %) max-temp))
                                 reports)]
            (if (empty? filtered)
              (println "No matching reports found. (Tip: Make sure you're using the correct unit: Celsius or Fahrenheit.)")
              (view-weather-reports filtered)))))

      :else
      (println "Invalid option."))))



(defn transform-weather-reports
  "Transforms weather data by converting temperature units."
  [reports]
  (println "Choose transformation:")
  (println "1. Convert Celsius to Fahrenheit")
  (println "2. Convert Fahrenheit to Celsius")
  (print "Enter your choice: ") (flush)
  (let [choice (read-line)]
    (cond
      (= choice "1")
      (map #(-> %
                (assoc :temperature (int (+ (* 1.8 (:temperature %)) 32)))
                (assoc :unit "F")) reports)

      (= choice "2")
      (map #(-> %
                (assoc :temperature (int (* 5/9 (- (:temperature %) 32))))
                (assoc :unit "C")) reports)

      :else
      (do (println "Invalid option. No transformation applied.")
          reports))))


(defn weather-statistics
  "Prints stats: average temp, hottest, coldest, unique conditions."
  [reports]
  (let [temps (map :temperature reports)
        avg (/ (reduce + temps) (count temps))
        hottest (apply max-key :temperature reports)
        coldest (apply min-key :temperature reports)
        conditions (set (map :condition reports))
        unit-h (or (:unit hottest) "C")
        unit-c (or (:unit coldest) "C")]
    (println (format "Average temperature: %.2f" (double avg)))
    (println (format "Hottest day:  %-12s | %-10s | %3d°%s | %-12s"
                     (:date hottest) (:location hottest) (:temperature hottest) unit-h (:condition hottest)))
    (println (format "Coldest day:  %-12s | %-10s | %3d°%s | %-12s"
                     (:date coldest) (:location coldest) (:temperature coldest) unit-c (:condition coldest)))
    (println (str "Unique conditions: " (count conditions)))))




(defn exit-program []
  (println "\nThank you for using the Weather Report System. Goodbye!")
  (System/exit 0))

(defn main-menu
  ([file]
   (main-menu file (load-reports file)))
  ([file reports]
   (println "\n=== Weather Report System ===")
   (println "1. View Weather Reports")
   (println "2. Transform Weather Report")
   (println "3. Filter Weather Reports")
   (println "4. Weather Statistics")
   (println "5. Save and Exit")
   (print "Enter your choice (1-5): ")
   (flush)
   (let [choice (read-line)]
     (handle-choice choice reports file))))

(defn handle-choice [choice reports file]
  (case choice
    "1" (do (view-weather-reports reports)
            (main-menu file reports))
    "2" (let [updated (transform-weather-reports reports)]
          (view-weather-reports updated)
          (main-menu file updated))
    "3" (do (filter-weather-reports reports)
            (main-menu file reports))
    "4" (do (weather-statistics reports)
            (main-menu file reports))
    "5" (do
          (println "Would you like to save the reports before exiting? (y/n): ")
          (flush)
          (when (= "y" (read-line))
            (save-reports reports))
          (exit-program))
    (do (println "Invalid option. Try again.")
        (main-menu file reports))))

;; Entry point
(defn -main [& args]
  (let [file "weather_data.txt"]
    (main-menu file)))

(-main)

