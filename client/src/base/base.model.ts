export abstract class BaseModel {
  deserialize(input: any = {}): this {
    const camelized = this.camelizeKeys(input);
    Object.assign(this, camelized);
    return this;
  }

  protected snakeCaseKeys(obj: any): any {
    if (!obj || typeof obj !== "object") return obj;
    if (Array.isArray(obj)) return obj.map((v) => this.snakeCaseKeys(v));

    const result: any = {};
    for (const key in obj) {
      const value = obj[key];
      const snakeKey = key.replace(/[A-Z]/g, (c) => `_${c.toLowerCase()}`);
      result[snakeKey] = this.snakeCaseKeys(value);
    }
    return result;
  }

  toServer(): any {
    const serverData = this.getData?.();
    if (!serverData) return {};
    return this.snakeCaseKeys(serverData);
  }

  protected getData?(): any;

  private camelizeKeys(obj: any): any {
    if (!obj || typeof obj !== "object") return obj;
    const result: any = {};
    for (const key in obj) {
      const camelKey = key.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
      result[camelKey] = obj[key];
    }
    return result;
  }
}
