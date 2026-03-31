// types.ts
export type EngineType = 'cpu' | 'gpu';

export interface EngineConfig {
  type: EngineType;
  threads: number;
  // Add more config properties as needed
}

export type EngineInitFunction = (config: EngineConfig) => Promise<Engine>;

export interface Engine {
  start(): Promise<void>;
  stop(): Promise<void>;
  // Add more engine methods as needed
}