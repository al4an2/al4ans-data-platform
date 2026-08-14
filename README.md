# Al4an's Data Platform

An open **lakehouse** built on the same stack fintech data platform teams run in production:
ingestion → raw on object storage (S3 / MinIO) → **Spark** → **Parquet** → **Apache Iceberg** → **Trino** for query.

The goal is to build the **Python services on top of it** that a
platform team actually owns — an ingestion framework, an Iceberg table-maintenance service, data contracts,
and quality/observability — under a Data Mesh model where domain teams own their data products.

## Status

🟢 Lakehouse infrastructure is live: MinIO + Nessie (Iceberg REST catalog, RocksDB-backed) + Trino
in Docker Compose, with the full write/read cycle verified end-to-end through Trino.

🚧 Phase 0 in progress: synthetic data generator (`datagen`) and the first Spark job
writing `bronze.transactions`.

## Quickstart

Prerequisites: Docker with Compose v2.

```bash
# 1. Local MinIO credentials (never committed)
cp docker/.env.example docker/.env        # edit values if you want

# 2. Start the lakehouse; wait until `docker compose ps` shows every service healthy
cd docker && docker compose up -d

# 3. Smoke-test the full write/read path (Trino -> Nessie -> MinIO)
docker compose exec trino trino --execute "
  CREATE SCHEMA IF NOT EXISTS lakehouse.smoke;
  CREATE TABLE IF NOT EXISTS lakehouse.smoke.t (id int);
  INSERT INTO lakehouse.smoke.t VALUES (1);
  SELECT count(*) FROM lakehouse.smoke.t;"
```

| UI | URL | Login |
|----|-----|-------|
| Trino query monitor | http://localhost:8080/ui/ | any username, no password |
| MinIO console | http://localhost:9001 | credentials from `docker/.env` |
| Nessie catalog (commits, branches) | http://localhost:19120 | no auth (local only) |

Python toolchain: `uv sync`, then `uv run pytest` / `uv run ruff check .` / `uv run mypy`.
Operations & troubleshooting: `docs/runbook.md`. Architecture decisions: `docs/adr/`.

## Planned phases

| Phase | Focus |
|-------|-------|
| 0 | Skeleton: MinIO + REST catalog + Trino + one Spark job → one Iceberg table |
| 1 | Python ingestion framework — declarative pydantic source specs → Spark jobs; idempotency, late data |
| 2 | Table Maintenance Service — compaction, snapshot expiry, orphan-file cleanup, metrics |
| 3 | Data products — contracts, quality gates, dbt-on-Trino marts, GDPR row-level deletes |
| 4 | Orchestration (Airflow) + observability (freshness / completeness) |

Early phases use **synthetic data generators**; a CDC feed from a real OLTP source is a later, optional extension.

## Stack

Python · Apache Spark · Apache Iceberg · Trino · Parquet · MinIO (S3-compatible) · Docker Compose
