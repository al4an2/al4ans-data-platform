# Al4an's Data Platform

An open **lakehouse** built on the same stack fintech data platform teams run in production:
ingestion → raw on object storage (S3 / MinIO) → **Spark** → **Parquet** → **Apache Iceberg** → **Trino** for query.

The goal is to build the **Python services on top of it** that a
platform team actually owns — an ingestion framework, an Iceberg table-maintenance service, data contracts,
and quality/observability — under a Data Mesh model where domain teams own their data products.

## Status

🚧 Phase 0 — bootstrapping the repository and a first vertical slice.

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
