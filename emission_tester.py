import hyperfetch.tuning as hf
from codecarbon import OfflineEmissionsTracker

'''def offline(config_path: str, country_iso: str, region: str | None,
            cloud_provider: str | None, cloud_region: str | None):
    tracker = OfflineEmissionsTracker(country_iso_code=country_iso, region=region,
                                      cloud_provider=cloud_provider,
                                      cloud_region=cloud_region)
    tracker.start()
    hf.tune(config_path)
    tracker.stop()
'''

if __name__ == '__main__':
    # Testing countries against each other
    hf.offline(config_path="tuning_parameters.yml", country_iso="DEU",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="DEU",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="AUS",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="AUS",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="ESP",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="ESP",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="IND",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="IND",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region=None, cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region=None, cloud_provider=None, cloud_region=None)

    # Regions agains each other US
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region="KY", cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region="Kentucky", cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region="VT", cloud_provider=None, cloud_region=None)
    hf.offline(config_path="tuning_parameters.yml", country_iso="USA",
               region="Vermont", cloud_provider=None, cloud_region=None)

    # Cloud providers against each other
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="asia-east2")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="australia-southeast1")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="europe-west2")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="southamerica-east1")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="us-central1")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="gcp", cloud_region="europe-west3")

    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="aws", cloud_region="ap-east-1")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="aws", cloud_region="ap-southeast-2")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="aws", cloud_region="eu-west-2")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="aws", cloud_region="sa-east-1")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="aws", cloud_region="eu-central-1")

    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="azure", cloud_region="eastasia")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="azure", cloud_region="australiaeast")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="azure", cloud_region="brazilsouth")
    hf.offline(config_path="tuning_parameters.yml", country_iso=None,
               region=None, cloud_provider="azure", cloud_region="centralus")