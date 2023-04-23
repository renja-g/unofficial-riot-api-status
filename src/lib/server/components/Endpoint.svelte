<script context="module" lang="ts">
  export interface Props {
    endpoint: {
      name: string;
      url: string;
      regions: { name: string; url: string }[];
    };
    region: { name: string; url: string };
    status?: "OK" | "Error";
  }

  export let endpoint: Props["endpoint"];
  export let region: Props["region"];
  export let status: Props["status"];

  async function fetchStatus() {
    try {
      let response = await fetch(region.url);
      if (response.ok) {
        status = "OK";
      } else {
        status = "Error";
      }
    } catch (error) {
      status = "Error";
    }
  }

  fetchStatus();
</script>

<div>
  <h3>{endpoint.name} ({region.name})</h3>
  <p>Status: {status}</p>
</div>
