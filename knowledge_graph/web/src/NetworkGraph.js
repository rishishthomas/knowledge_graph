import React, { useEffect, useRef } from 'react';
import { Network } from 'vis-network/standalone/esm/vis-network';

const NetworkGraph = ({ data }) => {
  const networkContainer = useRef(null);

  useEffect(() => {
    if (networkContainer.current) {
      const networkData = {
        nodes: data.nodes.map((node) => ({
          id: node.id,
          label: node.label,
        })),
        edges: data.edges.map((edge) => ({
          from: edge.from,
          to: edge.to,
          label: edge.label,
        })),
      };

      const options = {
        nodes: {
          shape: 'dot',
          size: 16,
          font: {
            size: 16,
          },
          borderWidth: 2,
        },
        edges: {
          width: 2,
          color: { inherit: true },
          smooth: true,
        },
        physics: {
          enabled: true,
          forceAtlas2Based: {
            gravitationalConstant: -26,
            centralGravity: 0.005,
            springLength: 230,
            springConstant: 0.18,
          },
          maxVelocity: 146,
          solver: 'forceAtlas2Based',
          timestep: 0.35,
          stabilization: { iterations: 150 },
        },
      };

      const network = new Network(networkContainer.current, networkData, options);

      return () => {
        network.destroy();
      };
    }
  }, [data]);

  return <div ref={networkContainer} style={{ height: '400px', width: '100%' }} />;
};

export default NetworkGraph;
