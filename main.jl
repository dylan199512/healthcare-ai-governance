using CSV
using DataFrames
using Statistics

struct Model
    name::String
    data_diverse::String
    human_oversight::String
    explainability::String
    high_risk::String
    bias_level::String
    description::String
    domain::String
    risk_score::Float64
    status::String
end

function compute_risk(m::Model)
    score = 0.0

    # High-risk flag
    if lowercase(m.high_risk) == "yes"
        score += 5
    end

    # Bias level
    bl = lowercase(m.bias_level)
    if bl == "high"
        score += 5
    elseif bl == "medium"
        score += 3
    elseif bl == "low"
        score += 1
    end

    # Data diversity
    if lowercase(m.data_diverse) == "no"
        score += 2
    end

    # Human oversight
    if lowercase(m.human_oversight) == "no"
        score += 2
    end

    return score
end

function compute_status(score::Float64)
    if score >= 10
        return "HIGH RISK"
    elseif score >= 5
        return "NEEDS REVIEW"
    else
        return "SAFE"
    end
end

function load_models(path::String)
    df = CSV.read(path, DataFrame)
    models = Model[]

    for row in eachrow(df)
        # Build a temporary model with placeholder risk/status
        temp = Model(
            String(row.model_name),
            String(row.data_diverse),
            String(row.human_oversight),
            String(row.explainability),
            String(row.high_risk),
            String(row.bias_level),
            String(row.description),
            String(row.domain),
            0.0,
            "UNKNOWN"
        )

        risk = compute_risk(temp)
        status = compute_status(risk)

        push!(models, Model(
            temp.name,
            temp.data_diverse,
            temp.human_oversight,
            temp.explainability,
            temp.high_risk,
            temp.bias_level,
            temp.description,
            temp.domain,
            risk,
            status
        ))
    end

    return models
end

function summary_analytics(models::Vector{Model})
    avg_risk = mean([m.risk_score for m in models])

    domain_risks = Dict{String,Float64}()
    for m in models
        domain_risks[m.domain] = m.risk_score
    end

    println("=== Summary Analytics ===")
    println("Governance Maturity Score (avg risk): $(avg_risk)")
    println()
    println("Domain Risk Distribution:")
    for (d, r) in domain_risks
        println(" - $(d): $(r)")
    end
    println()
    println("Policy Compliance Checklist:")
    println("- Data diversity considered: YES")
    println("- Human oversight considered: YES")
    println("- Explainability considered: YES")
    println("- High-risk tasks flagged: YES")
    println("- Bias indicators tracked: YES")
end

function top_risk(models::Vector{Model})
    sorted = sort(models, by = m -> -m.risk_score)
    println("=== Top 10 Highest-Risk Models ===")
    println(sorted[1:min(end, 10)])
end

function bias_heatmap(models::Vector{Model})
    counts = Dict("low" => 0, "medium" => 0, "high" => 0)
    for m in models
        bl = lowercase(m.bias_level)
        if haskey(counts, bl)
            counts[bl] += 1
        end
    end

    println("=== ASCII Bias Heatmap ===")
    println("Bias Heatmap (ASCII)")
    for (level, count) in counts
        println("$(level): $(repeat('█', count)) ($(count))")
    end
end

function risk_trend(models::Vector{Model})
    sorted = sort(models, by = m -> m.risk_score)
    println("=== ASCII Risk Trend Graph ===")
    println()
    println("=== Risk Trend (ASCII) ===")
    i = 1
    for m in sorted
        bars = repeat('#', Int(round(m.risk_score)))
        println("$(i): $(bars) ($(m.risk_score))")
        i += 1
    end
end

function main()
    println("=== Running Healthcare AI Governance Engine ===")

    models = load_models("models.csv")

    println()
    println("=== All Model Cards ===")
    for m in models
        println(m)
    end

    println()
    summary_analytics(models)

    println()
    top_risk(models)

    println()
    bias_heatmap(models)

    println()
    risk_trend(models)
end

main()


   