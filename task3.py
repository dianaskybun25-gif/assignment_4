experiments_data = [
{"method": "Euler", "iteration": 1, "error": 0.15,
"time_ms": 1.2},
{"method": "Runge-Kutta", "iteration": 1, "error": 0.01,
"time_ms": 3.5},
{"method": "Euler", "iteration": 2, "error": 0.18,
"time_ms": 1.3},
{"method": "Runge-Kutta", "iteration": 2, "error": 0.008,
"time_ms": 3.6},
{"method": "Euler", "iteration": 3, "error": 0.22,
"time_ms": 1.2},
{"method": "Newton", "iteration": 1, "error": 0.05,
"time_ms": 2.1}
]

def analyze_methods(data):
    statistics = {}
    #--------------------
    n = []
    e = []
    r = []
    o = [n,e,r]
    for method in data:
        if method["method"] == "Euler":
            e.append(method)
        if method["method"] == "Runge-Kutta":
            r.append(method)
        if method["method"] == "Newton":
            n.append(method)
    #------------------------------
    for i in o:
        stat = {}
        iterations = len(i)
        stat["iterations_count"] = iterations
        tot_time = 0
        for j in i:
            tot_time += j["time_ms"]
        stat["total_time_ms"] = tot_time
        er = [j["error"] for j in i]
        m_error = max(er)
        stat["max_error"] = m_error
        #----------------------------
        if i == n:
            statistics["Newton"] = stat
        if i == e:
            statistics["Euler"] = stat
        if i == r:
            statistics["Runge-Kutta"] = stat
        #----------------------------
    return statistics

statistics_1 = analyze_methods(experiments_data)
#for method in statistics_1:
    #print(method, statistics_1[method])

def analyze_methods_update(data):
    statistics_2 = {}
    methods = {}
    for method in data:
        method_name = method["method"]
        if method_name not in methods:
            methods[method_name] = []
        methods[method_name].append(method)
    for i in methods:
        stat = {}
        stat["iterations_count"] = len(methods[i])
        time_ms = 0
        er = []
        for j in methods[i]:
            time_ms += j["time_ms"]
            er.append(j["error"])
        stat["total_time_ms"] = time_ms
        stat["max_error"] = max(er)
        statistics_2[i] = stat
    return statistics_2


statistics_up = analyze_methods_update(experiments_data)
for method in statistics_up:
    print(method, statistics_up[method])

print("-------------------------------------------------------------------")

def analyze_methods_eff(data):
    statistics_e = {}
    methods = {}
    for method in data:
        method_name = method["method"]
        if method_name not in methods:
            methods[method_name] = []
        methods[method_name].append(method)
    for i in methods:
        stat = {}
        error_av = 0
        time = 0
        for j in methods[i]:
            error_av += j["error"]
            time += j["time_ms"]
        error_av = round(error_av / len(methods[i]), 2)
        speed_av = round(len(methods[i])/time, 2)
        stat["Середня швидкість обрахунку"] = speed_av
        stat["Середня величина помилки"] = error_av
        statistics_e[i] = stat
    return statistics_e
a = analyze_methods_eff(experiments_data)
for method in a:
    print(method, a[method])
s = []
e = []
for v in a.values():
    s.append(v["Середня швидкість обрахунку"])
    e.append(v["Середня величина помилки"])
max_s = max(s)
min_e = min(e)
for i in a:
    if a[i]["Середня величина помилки"] == min_e:
        print(f"Мін. середня похибка методу: {i} methods - {a[i]["Середня величина помилки"]}")
    if a[i]["Середня швидкість обрахунку"] == max_s:
        print(f"Макс.середня швидкість методу: {i} methods - {a[i]["Середня швидкість обрахунку"]}")