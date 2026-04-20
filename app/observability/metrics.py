
# app/observability/metrics.py

metrics = {
    "total_tickets": 0,
    "fallback_used": 0,
    "human_review": 0
}


def increment(key: str):
    metrics[key] += 1


def get_metrics():
    return metrics